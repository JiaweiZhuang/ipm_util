import xml.etree.ElementTree as ET
import pandas as pd


def get_single_rank(child_node):
    """
    Extract MPI info from IPM XML child node (corresponding to one MPI rank)

    child_node : xml.etree.ElementTree.Element
        child of root node, i.e. ET.parse(filename).getroot()[i]
    """
    i_regions = 6  # "regions" block under root.child

    mpi_node = child_node[i_regions][0]   # "region" block under root.child.regions

    record_list = []
    for leaf in mpi_node[1:]:  # skip the first "modules" tag
        record = {**leaf.attrib, 'time': float(leaf.text)}
        record_list.append(record)

    return record_list


def log_to_dataframe(filename):
    """
    Parse IPM XML log into pandas Dataframe

    filename : str
        path to IPM XML log file
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    df_list = []
    for child in root[1:]:
        mpi_temp = get_single_rank(child)
        rank = child.attrib['mpi_rank']

        df_temp = pd.DataFrame.from_records(mpi_temp).set_index('name')
        df_row = df_temp[['time']].T
        df_row.index = [rank]

        df_list.append(df_row)

    df_all = pd.concat(df_list, axis=0, join="outer", sort=False)
    df_all.index.name = 'rank'
    return df_all
