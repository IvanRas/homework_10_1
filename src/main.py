import logging
import os
import re

from typing import Any, List
from src.utils import get_transactions_dictionary, get_transactions_dictionary_excel, get_transactions_dictionary_csv

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s: %(filename)s: %(levelname)s: %(message)s",
    filename="../logs/main.log",
    filemode="w",
)

auth_logger = logging.getLogger("app.auth")


# выбор типа фаила для чтения
def main():
    """ """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями. ")
    print(f'''Выберите необходимый пункт меню:\n
    1. Получить информацию о транзакциях из JSON-файла\n
    2. Получить информацию о транзакциях из CSV-файла\n
    3. Получить информацию о транзакциях из XLSX-файла\n
    ''')
    user_input = input()
    if user_input.isdigit():
        number = int(user_input)
        if number == 1:
            auth_logger.info("Для обработки выбран JSON-файл.")
            transactions_info = get_transactions_dictionary(os.path.join("data", "operations.json)"))
        elif number == 2:
            auth_logger.info("Для обработки выбран CSV-файла.")
            # transactions_info = get_transactions_dictionary_csv(os.path.join("data", "transactions.csv"))
            transactions_info = get_transactions_dictionary_csv()
        elif number == 3:
            auth_logger.info("Для обработки выбран XLSX-файла.")
            # transactions_info = get_transactions_dictionary_excel(os.path.join("data", "transactions_excel.xlsx"))
            transactions_info = get_transactions_dictionary_excel()
        else:
            auth_logger.info("Не выбран тип файла")
            print("Вы ввели не число.")
    else:
        auth_logger.info("Не выбран тип файла")
        print("Вы ввели не число.")
    filter_state_list = filter_funct(transactions_info)
    print(filter_state_list)
    sort_list = funct_sort(filter_state_list)
    print(sort_list)
    rub_list = rub_sort(sort_list)
    print(rub_list)
    result = str_sort(rub_list)
    print(result)


# в выбраном типе фаила производится фильрация по столбцу "state"
# выббераем только те где state == filters
def filter_funct(transactions_info: dict) -> list[Any] | dict:
    """Фильтрация по стаусу """
    filters = str(input("""Введите статус, по которому необходимо выполнить фильтрацию.\n
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n""")).upper()
    filter_state_list_trans = []
    for i in transactions_info:
        if filters and i["state"] == "EXECUTED":
            auth_logger.info("Фильтрация по статусу: EXECUTED")
            filter_state_list_trans.append(i)  # создаем новый отфильтрованый список
            return filter_state_list_trans
        elif filters and i["state"] == "CANCELED":
            auth_logger.info("Фильтрация по статусу: CANCELED")
            filter_state_list_trans.append(i)
            return filter_state_list_trans
        elif filters and i["state"] == "PENDING":
            auth_logger.info("Фильтрация по статусу: PENDING")
            filter_state_list_trans.append(i)
            return filter_state_list_trans
        else:
            auth_logger.info("Не выбран тип фильтрации")
            return filter_funct(transactions_info)  # во всех других вариантах перезапуск функций


def funct_sort(filter_state_list_trans: dict) -> dict:
    # print("Отсортировать операции по дате? Да/Нет")
    s_data = str(input("Отсортировать операции по дате? Да/Нет\n")).lower()
    if s_data == "да":
        s_upp = str(input("Отсортировать по возрастанию или по убыванию?\n")).lower()
        if s_upp == "по возрастанию":
            return filter_state_list_trans["data"].sort  # возвращаут список отсортированный по дате возрастания
        elif s_upp == "по убыванию":
            return filter_state_list_trans["data"].sort(reverse=True)  # возвращаут список отсортированный по дате
        # убывания
        else:
            print("Выбрано не коректное значение")
            return filter_state_list_trans  # возвращаут не отсортированный список

    else:
        return filter_state_list_trans  # возвращает не измененный список


def rub_sort(filter_state_list_trans: dict) -> list[Any] | dict:
    s_rub = str(input("Выводить только рублевые тразакции? Да/Нет\n")).lower()
    filter_state_list_trans_ = []
    if s_rub == "да":
        for i in filter_state_list_trans:
            if i.get("currency_code") == "RUB" or (i.get("operationAmount") and i["operationAmount"]["currency"]["code"] == "RUB"):
                filter_state_list_trans_.append(i)
            return filter_state_list_trans_
    else:
        filter_state_list_trans_ = filter_state_list_trans
        return filter_state_list_trans_


def str_sort(filter_state_list_trans_: dict) -> list[Any] | dict:
    found_operations = []
    s_string = str(input("""Отфильтровать список транзакций по определенному слову
в описании? Да/Нет\n""")).lower()
    if s_string == "да":
        commit = str(input()).lower()
        for operation in filter_state_list_trans_:
            if re.search(commit, operation.get("description", "")):
                found_operations.append(operation)
        return found_operations
    return filter_state_list_trans_


# def str_sort(filter_state_list_trans_: list[dict], search_string: str) -> list[dict]:
#     found_operations = []
#     for operation in filter_state_list_trans_:
#         if re.search(search_string, operation.get("description", "")):
#             found_operations.append(operation)
#     return found_operations


if __name__ == "__main__":
    main()
