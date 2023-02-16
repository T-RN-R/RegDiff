from enum import Enum
import pprint
import argparse
from windows import RegHiveDictView
import pyregf
import os
from mdutils.tools.Table import Table
from mdutils.mdutils import MdUtils
import pathlib
import functools
from reporting.serializers import SystemHiveSerializer
from reporting.visitors import CoreReportMarkdownVisitor

import struct


DEBUG = False
ROOT_REG_DIR = "Windows\\System32\\config"
HIVE_NAMES = [
    # "SOFTWARE",
    # "COMPONENTS",
    "SYSTEM",
    # "DRIVERS",
]


class MarkdownSerializer():
    def __init__(self, output_file: str):
        self.output_file = output_file
        self.md = None

    def serialize(self, data: dict, title: str, single_diff: bool = False, no_diff: bool = False):
        self.md = MdUtils('example', title)
        if single_diff:
            if no_diff:
                self.md.new_header(1, "Full Dump")
            else: 
                self.md.new_header(1, "")

            self.do_hives(data,no_diff)
        else:
            for edition, hives in data.items():
                self.md.new_header(1, edition)
                self.do_hives(hives)
        self.md.new_table_of_contents("Table of contents", 5)
        with open(self.output_file, "w+") as f:
            f.write(self.md.get_md_text())

    def do_hives(self, hives: dict, no_diff:bool =False):
        for hive_name, diffs in hives.items():
            if hive_name == "SYSTEM":
                self.md.new_header(2, hive_name)
                self.md = SystemHiveSerializer().deserialize(
                    diffs, no_diff).to_markdown(self.md, CoreReportMarkdownVisitor())
            else:
                raise Exception(f"{hive_name} reporting is unsupported")


def main(argv=None):
    parser = cli()
    args = vars(parser.parse_args())
    if "func" in args.keys():
        func = args["func"]
        args.pop("func")
        func(**args)
    else:
        parser.print_help()


def cli_hive(hive_type, report_title, json_file, report_file, src):
    src_reg = pathlib.Path(src)
    hive_results = {}

    regA = pyregf.file()
    regA.open(str(src_reg)
              )
    #src = processRoot(regA.get_root_key())
    src = RegHiveDictView(regA.get_root_key())
    hive_results[hive_type] = src

    md_serializer = MarkdownSerializer(report_file)
    md_serializer.serialize(
        data=hive_results, title=report_title,single_diff=True, no_diff=True)

    if json_file:
        import json
        with open(json_file, "w+", encoding="utf-8") as f:
            f.write(str(hive_results))



def cli_diff(hive_type, report_title, json_file, report_file, src, dst):
    src_reg = pathlib.Path(src)
    dst_reg = pathlib.Path(dst)

    hive_results = {}
    # open the files
    regA = pyregf.file()
    regB = pyregf.file()

    regA.open(str(src_reg))
    regB.open(str(dst_reg))
    # process the registry
    src = processRoot(regA.get_root_key())
    dest = processRoot(regB.get_root_key())

    added = {}
    removed = {}
    modified = {}

    for k, v in src.items():
        if k not in dest.keys():
            removed[k] = v
            continue
        if dest[k] != v:
            modified[k] = {"src": v, "dst": dest[k]}

    for k, v in dest.items():
        if k not in src.keys():
            added[k] = v

    j = {"added": added, "removed": removed, "modified": modified}
    hive_results[hive_type] = j

    md_serializer = MarkdownSerializer(report_file)
    md_serializer.serialize(
        data=hive_results, title=report_title, single_diff=True)

    if json_file:
        import json
        with open(json_file, "w+", encoding="utf-8") as f:
            f.write(str(hive_results))


def cli_builddiff(report_title, json_file, report_file, iso, root_dir, src, dst):
    if iso:
        raise Exception("ISO files are currently unhandled.")
    src_uid_dir = pathlib.Path(root_dir, src)
    dst_uid_dir = pathlib.Path(root_dir, dst)

    src_editions = set(os.listdir(src_uid_dir))

    dst_editions = set(os.listdir(dst_uid_dir))

    editions_to_diff = list(src_editions.intersection(dst_editions))
    editions_to_diff.sort()
    print(f"Diffable editions: {editions_to_diff}")
    diff_result = {}
    if "Core" in editions_to_diff and "CoreN" in editions_to_diff:
        editions_to_diff.remove("CoreN")
    if "Professional" in editions_to_diff and "ProfessionalN" in editions_to_diff:
        editions_to_diff.remove("ProfessionalN")
    if "Professional" in editions_to_diff and "Core" in editions_to_diff:
        editions_to_diff.remove("Core")

    for edition in editions_to_diff:
        hive_results = {}
        for hive in HIVE_NAMES:
            print(f"Diffing {edition} editions {hive} hive")
            fileA = pathlib.Path(src_uid_dir, edition, ROOT_REG_DIR, hive)
            fileB = pathlib.Path(dst_uid_dir, edition, ROOT_REG_DIR, hive)
            # open the files
            regA = pyregf.file()
            regB = pyregf.file()

            regA.open(str(fileA))
            regB.open(str(fileB))
            # process the registry
            src = processRoot(regA.get_root_key())
            dest = processRoot(regB.get_root_key())

            # Print metrics on how many we managed to remove
            """
            if DEBUG:
                report(len(src),'count-A: ')    
                report(len(src.difference(dest)),'count-A !B: ')
            
            report(src.difference(dest), 'UNIQUE-A: {0}'.format(fileA))
            """
            added = {}
            removed = {}
            modified = {}

            for k, v in src.items():
                if k not in dest.keys():
                    removed[k] = v
                    continue
                if dest[k] != v:
                    modified[k] = {"src": v, "dst": dest[k]}

            for k, v in dest.items():
                if k not in src.keys():
                    added[k] = v

            j = {"added": added, "removed": removed, "modified": modified}
            hive_results[hive] = j
        diff_result[edition] = hive_results
        # break
    md_serializer = MarkdownSerializer(report_file)
    md_serializer.serialize(data=diff_result, title=report_title)

    if json_file:
        import json
        with open(json_file, "w+", encoding="utf-8") as f:
            f.write(str(diff_result))


def processRoot(root):
    '''
    Helper function to start recursive call
    @root: pyregf file's root key
    @return: set() containing all parsed registry keys/values
    '''
    coll = dict()
    for cur in root.sub_keys:
        processKey(cur, coll)
    return coll


class RegType(Enum):
    LIBREGF_VALUE_TYPE_UNDEFINED = 0
    LIBREGF_VALUE_TYPE_STRING = 1
    LIBREGF_VALUE_TYPE_EXPANDABLE_STRING = 2
    LIBREGF_VALUE_TYPE_BINARY_DATA = 3
    LIBREGF_VALUE_TYPE_INTEGER_32BIT_LITTLE_ENDIAN = 4
    LIBREGF_VALUE_TYPE_INTEGER_32BIT_BIG_ENDIAN = 5
    LIBREGF_VALUE_TYPE_SYMBOLIC_LINK = 6
    LIBREGF_VALUE_TYPE_MULTI_VALUE_STRING = 7
    LIBREGF_VALUE_TYPE_RESOURCE_LIST = 8
    LIBREGF_VALUE_TYPE_FULL_RESOURCE_DESCRIPTOR = 9
    LIBREGF_VALUE_TYPE_RESOURCE_REQUIREMENTS_LIST = 10
    LIBREGF_VALUE_TYPE_INTEGER_64BIT_LITTLE_ENDIAN = 11


def is_string_type(key):
    return (key == RegType.LIBREGF_VALUE_TYPE_STRING or key == RegType.LIBREGF_VALUE_TYPE_EXPANDABLE_STRING or key == RegType.LIBREGF_VALUE_TYPE_SYMBOLIC_LINK)


def processKey(key, coll, path=''):
    '''
    Recursive function loads set object with all the keys/values for a provided key & children
    @key: the pyregf key acting as starting point of recursion
    @coll: the set object to collect parsed info into
    @path: parent key's path string built by recursive calls
    '''

    KEYS_TO_IGNORE = ["DriverDatabase",  # Maybe handle these eventually. Differ can't handle the changes in hashes in the keys
                      "Control\\Power",  # Not very interesting
                      "Control\\OSExtensionDatabase",
                      # Maybe handle this eventually, these need to be reverse engineered
                      "Control\\Notifications",
                      "Control\\NetworkSetup",  # Likely not interesting
                      "Software\\Microsoft\\BuildLayers"  # Don't think its interesting
                      ]

    """     
    # To develop:

    "ControlSet001\\Control\\Cryptography"
    ControlSet001\\Control\\Class\\
    ControlSet001\\Control\\CI\\"
    ControlSet001\\Control\\Tpm
    ControlSet001\\Control\\SafeBoot
    ControlSet001\\Control\\Session Manager
    ControlSet001\\Control\\WMI\\Security
    ControlSet001\\Control\\FileSystem
    ControlSet001\\Control\\FeatureManagement
    
    """
    # print(key.get_name())
    # build & save printable key path
    expanded = os.path.join(path, key.get_name())
    coll[expanded] = None
    if IGNORE_SOME_KEYS:
        for ignore_key in KEYS_TO_IGNORE:
            if ignore_key in expanded:
                return
    for cur in key.values:  # build & save printable value record paths
        curName = cur.get_name()
        data = None
        try:
            t = RegType(cur.get_type())
            if is_string_type(t):
                data = cur.get_data_as_string()
            elif t == RegType.LIBREGF_VALUE_TYPE_INTEGER_32BIT_BIG_ENDIAN:
                data = struct.unpack(">I", cur.get_data())[0]
            elif t == RegType.LIBREGF_VALUE_TYPE_INTEGER_32BIT_LITTLE_ENDIAN:
                data = struct.unpack("<I", cur.get_data())[0]
            elif t == RegType.LIBREGF_VALUE_TYPE_INTEGER_64BIT_LITTLE_ENDIAN:
                data = struct.unpack("<Q", cur.get_data())[0]
            elif cur.get_data() is not None:
                data = cur.get_data()
            else:
                data = None
        except ValueError as e:
            # bug in pyregf?
            if cur.get_data() is not None:
                data = cur.get_data()
            else:
                data = None

        # data = cur.get_data()
        if curName is None:
            curName = '(Default)'
        tmpStr = '{}'.format(curName)
        tmpPath = os.path.join(expanded, tmpStr)
        coll[tmpPath] = data

    for cur in key.sub_keys:  # recursive call on each subkey
        processKey(cur, coll, expanded)


def report(reportSet, reportName):
    # print a well formatted report
    print(reportName)
    pprint.pprint(reportSet, indent=2)
    print()


IGNORE_SOME_KEYS = True


def parseArgs(argv):
    '''
    Parse cmd line arguments
    @argv: array of command line arguments
    '''
    import argparse
    parser = argparse.ArgumentParser(
        description='Prints registryA.difference(registryB)')
    parser.add_argument(
        '--debug', help='Print debugging statements.', action='store_true')
    parser.add_argument('--output_file', help='Print debugging statements.')

    parser.add_argument('fileA', type=str,
                        help='Primary registry file to diff with')
    parser.add_argument('fileB', type=str,
                        help='Second registry file to diff with')
    args = parser.parse_args()

    # Set global debug value
    global DEBUG
    DEBUG = args.debug

    # return the filenames
    return os.path.abspath(args.fileA), os.path.abspath(args.fileB), os.path.abspath(args.output_file)


def cli():
    parser = argparse.ArgumentParser(
        description='Generates reports on the Windows registry', add_help=False)

    subs = parser.add_subparsers(help="The sub module to run:")
    diff_parser = subs.add_parser('diff', help="Diffs two registry hives")
    # Takes hive_src and hive_dst and diffs them
    diff_parser.add_argument(
        "--hive_type", help="Type of hive to diff [SYSTEM, SOFTWARE etc...]", type=str)
    diff_parser.add_argument("--report-title", type=str,
                             help="Title of the markdown report")
    diff_parser.add_argument(
        "--json-file", type=str, help="Output file for the JSON dump", required=False)
    diff_parser.add_argument("--report-file", type=str,
                             help="Output file for the markdown report")
    diff_parser.add_argument('src', type=str,
                             help='Source registry file to diff ')
    diff_parser.add_argument('dst', type=str,
                             help='Destination registry file to diff ')
    diff_parser.set_defaults(func=cli_diff)

    builddiff_parser = subs.add_parser(
        'builddiff', help="Diffs two extracted install.wim files")
    builddiff_parser.add_argument(
        "--report-title", type=str, help="Title of the markdown report")
    builddiff_parser.add_argument(
        "--json-file", type=str, help="Output file for the JSON dump", required=False)
    builddiff_parser.add_argument(
        "--report-file", type=str, help="Output file for the markdown report")
    builddiff_parser.add_argument(
        "--iso", help="Indicates if the target dirs are ISO files", required=False)
    builddiff_parser.add_argument(
        '--root_dir', help='Print debugging statements.')
    builddiff_parser.add_argument(
        'src', type=str, help='Primary folder or ISO to diff with')
    builddiff_parser.add_argument(
        'dst', type=str, help='Secondary folder or ISO to diff with')
    builddiff_parser.set_defaults(func=cli_builddiff)

    hive_parser = subs.add_parser(
        "hive", help="Takes a single hive and dumps all of the data")
    hive_parser.add_argument(
        "--hive_type", help="Type of hive to diff [SYSTEM, SOFTWARE etc...]", type=str)
    hive_parser.add_argument("--report-title", type=str,
                             help="Title of the markdown report")
    hive_parser.add_argument(
        "--json-file", type=str, help="Output file for the JSON dump", required=False)
    hive_parser.add_argument("--report-file", type=str,
                             help="Output file for the markdown report")
    hive_parser.add_argument(
        'src', type=str, help='Registry file to dump with')
    hive_parser.set_defaults(func=cli_hive)

    # iso extraction, wim extraction, folder lookup
    return parser


def parseArgs2(argv):
    '''
    Parse cmd line arguments
    @argv: array of command line arguments
    '''
    parser = argparse.ArgumentParser(
        description='Prints registryA.difference(registryB)')
    parser.add_argument('--output_file', help='Print debugging statements.')
    parser.add_argument('--root_dir', help='Print debugging statements.')
    parser.add_argument('src_uid', type=str,
                        help='Primary registry file to diff with')
    parser.add_argument('dst_uid', type=str,
                        help='Second registry file to diff with')
    parser.add_argument('--title', type=str,
                        help="Title of diff", default=None)
    args = parser.parse_args()

    if not args.title:
        args.title = f"{args.src_uid} -> {args.dst_uid} Diff"
    # return the filenames
    return args.src_uid, args.dst_uid, os.path.abspath(args.output_file), os.path.abspath(args.root_dir), args.title


if __name__ == '__main__':
    main()
