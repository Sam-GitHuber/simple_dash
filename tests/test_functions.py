"""
Testing module for functions.py
"""
# Standard imports
import pytest

# 3rd party imports
import pandas as pd

# Local imports
from src.functions import read_csv, select_stock

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
    assert (result.columns == expected.columns).all()
    assert result['group'].equals(expected['group'])
    assert result['target_stock'].equals(expected['target_stock'])
    assert result['target_fill_rate'].equals(expected['target_fill_rate'])

def test_select_stock_simple():
    """
    Simple test for selecting stock
    """
    data = pd.DataFrame({
        "group": ["A", "A", "B", "B"],
        "date": ["2021-01-01", "2021-01-02", "2021-01-01", "2021-01-02"],
        "quantity": [10, 20, 30, 40]
    })

    result = select_stock(data, "A")

    expected = pd.DataFrame({
        "group": ["A", "A"],
        "date": ["2021-01-01", "2021-01-02"],
        "quantity": [10, 20]
    })
    assert (result.columns == expected.columns).all()
    assert result['group'].equals(expected['group'])
    assert result['date'].equals(expected['date'])
    assert result['quantity'].equals(expected['quantity'])

def test_failing():
    """
    Failing test
    """
    assert True


if __name__ == '__main__':
    pytest.main()
