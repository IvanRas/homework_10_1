def filter_by_currency(transactions, currency):
    """Функция принимает на вход список со словарем и возвращает id операции"""
    for key in transactions:
        if key["operationAmount"]["currency"]["name"] == currency:
        # new_list = filtr(key["operationAmount"]["currency"]["name"] == currency ## фильтрация по имени валюты
            #return [new_list]  ## вывод нового отсортированого списка по имени валюты
            return ["id"] # нужно показать всю информайию по операций


def transaction_descriptions(transactions):
    """Функция принимает список словарей и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction.get("descriptions")


def card_number_generator(start, finish):
    for num in range(start, finish):
        pass
