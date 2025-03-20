"""
Module for common functions.
"""

import pathlib
import pandas as pd


def read_csv(file_name: str, **kwargs) -> pd.DataFrame:
    """
    Read a CSV file from the data directory.
    """
    file_path = pathlib.Path(__file__).parent.parent.joinpath("data", file_name)
    return pd.read_csv(file_path, **kwargs)


def select_stock(data: pd.DataFrame, stock_group: str) -> pd.DataFrame:
    """
    Select stock data for a given group.
    """
    return data[data['group'] == stock_group]
