def filter_by_currency(transactions, currency):
    """Функция возвращаtn итератор с операциями в заданной валюте."""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions):
    """Функция принимает список словарей и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction.get("descriptions")


def card_number_generator(start, finish):
    """генератор номеров банковских карт"""
    for i in range(start, finish + 1):
        empty_str = "0000000000000000"
        str_sum = empty_str + str(i)
        card_number = f"{str_sum[-16:-12]} {str_sum[-12:-8]} {str_sum[-8:-4]} {str_sum[-4:-1]}{str_sum[-1]}"
        yield card_number
