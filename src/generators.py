def filter_by_currency(transactions, currency: list) -> list:
    """Функция возвращаtn итератор с операциями в заданной валюте."""
    for key in transactions:
        my_list = []
        if key["operationAmount"]["currency"]["name"] == currency:
            my_list.append(filter(key["operationAmount"]["currency"]["name"], currency))
        return my_list


def transaction_descriptions(transactions: list) -> list:
    """Функция принимает список словарей и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction.get("descriptions")


def card_number_generator(start: int, finish: int) -> str:
    for num in range(start, finish):
        card_number = [i for i, card_number[:4] + card_number[4:8] + card_number[8:12] + card_number[-4:]
                       in enumerate([(1, 2), (4, 4), (5, 7), (0, 0)]) if i+1]
