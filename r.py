import pprint

import pyregf
import os
from mdutils.tools.Table import Table
from mdutils.mdutils import MdUtils
import pathlib, functools
from reporting.serializers import SystemHiveSerializer
from reporting.visitors import CoreReportMarkdownVisitor




DEBUG = False
ROOT_REG_DIR = "Windows\\System32\\config"
HIVE_NAMES = [
   # "SOFTWARE",
   # "COMPONENTS",
    "SYSTEM",
   # "DRIVERS",
]







class MarkdownSerializer():
    def __init__(self, output_file:str):
        self.output_file = output_file
        self.md = None





    def serialize(self, src_uid:str, dst_uid:str, data:dict):
        self.md = MdUtils('example', f"{src_uid} {dst_uid} Diff")
        for edition, hives in data.items():
            self.md.new_header(1, edition)
            for hive, diffs in hives.items():
                if hive == "SYSTEM":
                    self.md.new_header(2, hive)

                    self.md = SystemHiveSerializer().deserialize(diffs).to_markdown(self.md, CoreReportMarkdownVisitor())

                continue
                print(f"Writing {edition} {hive} hive")
                self.md.new_header(2, hive)
                for diff, data in diffs.items():
                    self.md.new_header(3, diff)
                    if diff == "modified":
                        for k, v in data.items():
                            self.md.new_header(4, k)
                            src = v.get("src")
                            if isinstance(src, bytes):
                                added_v = src.hex(sep=" ")
                            else:
                                added_v = str(src)
                            if added_v is None:
                                added_v = "null"
                            dst = v.get("dst")
                            if isinstance(dst, bytes):
                                dst_v = dst.hex(sep=" ")
                            else:
                                dst_v = str(dst)
                            if dst_v is None:
                                dst_v = "null"
                            self.md.new_table(2,2,["Source","Destination", f"`{added_v}`", f"`{dst_v}`"])


                    else:
                        for k, v in data.items():
                            if isinstance(v, bytes):
                                str_v = v.hex(sep=" ")
                            else:
                                str_v = str(v)
                            if str_v is None:
                                str_v = "null"
                            self.md.new_header(3, k)
                            self.md.insert_code(str_v)
                    
                
        


        self.md.new_table_of_contents("Table of contents", 4)

        with open(self.output_file, "w+") as f:
            f.write(self.md.get_md_text())


def main(argv=None):
    src_uid, dst_uid, output_file, root_dir = parseArgs2(argv)

    src_uid_dir = pathlib.Path(root_dir, src_uid)
    dst_uid_dir = pathlib.Path(root_dir, dst_uid)

    src_editions = set(os.listdir(src_uid_dir))


    dst_editions =set( os.listdir(dst_uid_dir))

    editions_to_diff = list(src_editions.intersection(dst_editions))
    editions_to_diff.sort()
    print(f"Diffing editions: {editions_to_diff}")
    diff_result = {}
    for edition in editions_to_diff:
        hive_results = {}
        for hive in HIVE_NAMES:
            print(f"Diffing {edition} editions {hive} hive")
            fileA = pathlib.Path(src_uid_dir,edition,ROOT_REG_DIR, hive)
            fileB = pathlib.Path(dst_uid_dir,edition,ROOT_REG_DIR, hive)
            #open the files
            regA = pyregf.file()
            regB = pyregf.file()
            
            regA.open(str(fileA))
            regB.open(str(fileB))
            #process the registry
            src = processRoot(regA.get_root_key())
            dest = processRoot(regB.get_root_key())


            #Print metrics on how many we managed to remove
            """
            if DEBUG:
                report(len(src),'count-A: ')    
                report(len(src.difference(dest)),'count-A !B: ')
            
            report(src.difference(dest), 'UNIQUE-A: {0}'.format(fileA))
            """
            added = {}
            removed = {}
            modified = {}
            
            for k,v in src.items():
                if k not in dest.keys():
                    removed[k] = v
                    continue
                if dest[k] != v:
                    modified[k] = {"src": v, "dst": dest[k]}

            for k, v in dest.items():
                if k not in src.keys():
                    added[k] = v

            j = {"added":added, "removed":removed, "modified": modified}
            hive_results[hive] = j
        diff_result[edition] = hive_results
        
    md_serializer = MarkdownSerializer(output_file)
    md_serializer.serialize(src_uid, dst_uid, data=diff_result)



    """
    import json
    with open(output_file, "w+") as f :
        json.dump( j,f)
    """




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

from enum import Enum   
class RegType(Enum):
    LIBREGF_VALUE_TYPE_UNDEFINED			= 0
    LIBREGF_VALUE_TYPE_STRING			= 1
    LIBREGF_VALUE_TYPE_EXPANDABLE_STRING		= 2
    LIBREGF_VALUE_TYPE_BINARY_DATA			= 3
    LIBREGF_VALUE_TYPE_INTEGER_32BIT_LITTLE_ENDIAN	= 4
    LIBREGF_VALUE_TYPE_INTEGER_32BIT_BIG_ENDIAN	= 5
    LIBREGF_VALUE_TYPE_SYMBOLIC_LINK		= 6
    LIBREGF_VALUE_TYPE_MULTI_VALUE_STRING		= 7
    LIBREGF_VALUE_TYPE_RESOURCE_LIST		= 8
    LIBREGF_VALUE_TYPE_FULL_RESOURCE_DESCRIPTOR	= 9
    LIBREGF_VALUE_TYPE_RESOURCE_REQUIREMENTS_LIST	= 10
    LIBREGF_VALUE_TYPE_INTEGER_64BIT_LITTLE_ENDIAN	= 11

def is_string_type(key):
    return (key ==RegType.LIBREGF_VALUE_TYPE_STRING or key == RegType.LIBREGF_VALUE_TYPE_EXPANDABLE_STRING or key == RegType.LIBREGF_VALUE_TYPE_SYMBOLIC_LINK)

import struct

def processKey(key, coll, path=''):
    '''
    Recursive function loads set object with all the keys/values for a provided key & children
    @key: the pyregf key acting as starting point of recursion
    @coll: the set object to collect parsed info into
    @path: parent key's path string built by recursive calls
    '''
    #print(key.get_name())
    #build & save printable key path
    expanded = os.path.join(path, key.get_name())
    coll[expanded] = None
    
    for cur in key.values: #build & save printable value record paths
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
            else: data = None
        except ValueError as e:
            #bug in pyregf?
            if cur.get_data() is not None:
                data = cur.get_data()
            else: data = None

        #data = cur.get_data()
        if curName is None:
            curName = '(Default)'
        tmpStr = '{}'.format(curName)
        tmpPath = os.path.join(expanded, tmpStr)
        coll[tmpPath] = data
        
    for cur in key.sub_keys: #recursive call on each subkey
        processKey(cur, coll, expanded)


def report(reportSet, reportName):
    #print a well formatted report
    print(reportName)
    pprint.pprint(reportSet, indent=2)
    print()

    
def parseArgs(argv):
    '''
    Parse cmd line arguments
    @argv: array of command line arguments
    '''
    import argparse
    parser = argparse.ArgumentParser(description='Prints registryA.difference(registryB)')
    parser.add_argument('--debug', help='Print debugging statements.', action='store_true')
    parser.add_argument('--output_file', help='Print debugging statements.')

    parser.add_argument('fileA', type=str, help='Primary registry file to diff with')
    parser.add_argument('fileB', type=str, help='Second registry file to diff with') 
    args = parser.parse_args()
    
    #Set global debug value
    global DEBUG
    DEBUG = args.debug
    
    #return the filenames
    return os.path.abspath(args.fileA), os.path.abspath(args.fileB), os.path.abspath(args.output_file)



def parseArgs2(argv):
    '''
    Parse cmd line arguments
    @argv: array of command line arguments
    '''
    import argparse
    parser = argparse.ArgumentParser(description='Prints registryA.difference(registryB)')
    parser.add_argument('--output_file', help='Print debugging statements.')
    parser.add_argument('--root_dir', help='Print debugging statements.')
    parser.add_argument('src_uid', type=str, help='Primary registry file to diff with')
    parser.add_argument('dst_uid', type=str, help='Second registry file to diff with') 
    args = parser.parse_args()
    
    
    #return the filenames
    return args.src_uid, args.dst_uid, os.path.abspath(args.output_file),os.path.abspath(args.root_dir)


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))