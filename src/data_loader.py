import pandas as pd

def load_data(file_path):
    """
    Laddar dataset från CSV fil och returnerar pandas DataFrame.
    """
    return pd.read_csv(file_path)