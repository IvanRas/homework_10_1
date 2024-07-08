import pytest
from src.processing import filter_by_state, sort_by_date, operations


@pytest.fixture
def test_operations():
    return 'EXECUTED'


@pytest.fixture
def test_operations_1():
    return operations
