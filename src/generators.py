from typing import Any


def filter_by_currency(transactions: dict, currency: str) -> Any:
    """Функция возвращаtn итератор с операциями в заданной валюте."""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: dict) -> Any:
    """Функция принимает список словарей и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction.get("descriptions")


def card_number_generator(start, finish) -> str:
    """генератор номеров банковских карт"""
    for i in range(start, finish + 1):
        empty_str = "000000000000000"
        str_sum = empty_str + str(i)
        card_number = f"{str_sum[:4]} {str_sum[4:8]} {str_sum[8:12]} {str_sum[12:]}"
        yield card_number
