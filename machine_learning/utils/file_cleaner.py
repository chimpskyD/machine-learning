import pandas as pd

standard_encoding = 'utf-8'
standard_sep = ';'

def open_csv_file(path):
    return pd.read_csv(path)

def replace_all_values_with_label(dataframe, old_value, new_value):
    cols = dataframe.columns.values.tolist()
    return dataframe.replace(old_value,new_value, inplace=True, cols=cols)


def replace_values_in_col_with_new_value(dataframe, file, col_name:str,  new_value, old_value=None):
    """" new_value can be a value or a dictionary,
    e.g. replacements = {1: 'Male', 2:'Female'}"""
    cols = dataframe.columns.values.tolist()
    if type(new_value) is dict and old_value is None:
        dataframe[col_name] = dataframe[col_name].replace(new_value)
        dataframe.to_csv(file, sep=standard_sep, encoding=standard_encoding, columns=cols)
    else:
        dataframe[col_name] = dataframe[col_name].replace(old_value,new_value)
        dataframe.to_csv(file, sep=standard_sep, encoding=standard_encoding, columns=cols)

def cols_to_drop(dataframe, file, to_drop):
    """to_drop must be an array of strings"""
    cols = dataframe.columns.values.tolist()
    dataframe.drop(to_drop, inplace=True, axis=1)
    dataframe.to_csv(file, sep=standard_sep, encoding=standard_encoding, columns=cols, index_label=False)

