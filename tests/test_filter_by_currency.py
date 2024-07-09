import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(transactions, currency):
     """тестирование  фильтра валютной операции"""
     assert filter_by_currency(transactions, "USD") == ["939719570", "142264268", "895315941"]


def test_transaction_descriptions(transactions):
    """тестирование функции описания"""
    transactions = [
        {"description": "Перевод организации"},
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод с карты на карту"},
        {"description": "Перевод организации"}
    ]
    description = list(transaction_descriptions(transactions))
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации"
    ]
    assert transactions == expected


def test_card_number_generator(start, end):

    number = next(card_number_generator(start, end))
    assert number == "0000 0000 0000 0001"
