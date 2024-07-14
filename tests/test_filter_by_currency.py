import pytest
from src.generators import filter_by_currency, card_number_generator


@pytest.fixture
def transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",  # состояние, статус
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {  # сумма операции
                "amount": "9824.07",  # количество, сумма
                "currency": {"name": "USD", "code": "USD"},  # валюта  # имя  # код
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def start():
    return 1


@pytest.fixture
def finish():
    return 1


@pytest.fixture
def currency():
    return "USD"


def test_filter_by_currency(transactions, currency):
    """тестирование фильтра валютной операции"""
    assert filter_by_currency(transactions, "USD") == ["939719570", "142264268", "895315941"]


def test_transaction_descriptions(transactions):
    """тестирование функции описания"""
    transactions = [
        {"description": "Перевод организации"},
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод с карты на карту"},
        {"description": "Перевод организации"}
    ]

    expected = [
        {"description": "Перевод организации"},
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод с карты на карту"},
        {"description": "Перевод организации"}
    ]
    assert transactions == expected


def test_card_number_generator(start, finish):
    """Тест генератор номеров банковских карт"""
    number = next(card_number_generator(start, finish))
    assert number == "0000 0000 0000 0001"
