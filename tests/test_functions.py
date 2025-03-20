"""
Testing module for functions.py
"""
# Standard imports
import pytest

# 3rd party imports
import pandas as pd
from pandas.testing import assert_frame_equal

# Local imports
from src.functions import read_csv

def test_read_csv_simple():
    """
    Simple test for read_csv
    """
    result = read_csv('targets.csv')

    
    expected = pd.DataFrame({
        "group": ["A", "B", "C"],
        "target_stock": [10, 100, 10],
        "target_fill_rate": [0.8, 0.9, 0.7]
    })
    assert assert_frame_equal(result, expected)

if __name__ == '__main__':
    pytest.main()
