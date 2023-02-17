from mdutils.tools.Table import Table
from mdutils.mdutils import MdUtils


def table_helper(md: MdUtils, headers, rows):
    assert (len(rows) % len(headers)) == 0, "You screwed up something somewhere!"
    num_cols = len(headers)
    num_rows = int(len(rows)/len(headers)) + 1
    table = headers+rows
    md.new_table(num_cols, num_rows, table)
