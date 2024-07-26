import pytest

from src.external_api import convert_from_i_to_rub


@pytest.fixture
def get_rub_transaction():
    return "RUB", 123.45


def test_convert_from_i_to_rub(get_rub_transaction):
    assert convert_from_i_to_rub("RUB", 123.45) == 123.45
