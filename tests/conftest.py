import pytest

from src.processing import operations


@pytest.fixture
def test_operations():
    return 'EXECUTED'


@pytest.fixture
def test_operations_1():
    return operations
