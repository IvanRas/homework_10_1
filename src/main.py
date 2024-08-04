import logging
import os
from typing import List, Any

from src.utils import get_transactions_dictionary, get_transactions_dictionary_excel, get_transactions_dictionary_csv

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s: %(filename)s: %(levelname)s: %(message)s",
    filename="../logs/main.log",
    filemode="w",
)

auth_logger = logging.getLogger("app.auth")


# выбор типа фаила для чтения
def maim() -> dict:
    """ """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями. ")
    print(f'''Выберите необходимый пункт меню:\n
    1. Получить информацию о транзакциях из JSON-файла\n
    2. Получить информацию о транзакциях из CSV-файла\n
    3. Получить информацию о транзакциях из XLSX-файла\n
    ''')
    i = int(input())
    if i == 1:
        auth_logger.info("Для обработки выбран JSON-файл.")
        transactions_info = get_transactions_dictionary(os.path.join("data", "operations.json)"))
        return transactions_info
    elif i == 2:
        auth_logger.info("Для обработки выбран CSV-файла.")
        # transactions_info = get_transactions_dictionary_csv(os.path.join("data", "transactions.csv"))
        transactions_info = get_transactions_dictionary_csv()
        return transactions_info
    elif i == 3:
        auth_logger.info("Для обработки выбран XLSX-файла.")
        # transactions_info = get_transactions_dictionary_excel(os.path.join("data", "transactions_excel.xlsx"))
        transactions_info = get_transactions_dictionary_excel()
        return transactions_info
    else:
        auth_logger.info("Не выбран тип файла")
        return maim()


# должны получить список для работы со следующими функциями


# в выбраном типе фаила производится фильрация по столбцу "state"
# выббераем только те где state == filters
def filter_funct(transactions_info: dict) -> list[Any] | dict:
    """Фильтрация по стаусу """
    filters = str(input("""Введите статус, по которому необходимо выполнить фильтрацию.\n
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")).upper()
    filter_state_list_trans = []
    for [state] in transactions_info:
        if filters == "EXECUTED":
            auth_logger.info("Фильтрация по статусу: EXECUTED")
            filter_state_list_trans.append()  # создаем новый отфильтрованый список
            return filter_state_list_trans
        elif filters == "CANCELED":
            auth_logger.info("Фильтрация по статусу: CANCELED")
            filter_state_list_trans.append()
            return filter_state_list_trans
        elif filters == "PENDING":
            auth_logger.info("Фильтрация по статусу: PENDING")
            filter_state_list_trans.append()
            return filter_state_list_trans
        else:
            auth_logger.info("Не выбран тип фильтрации")
            return filter_funct()  # во всех других вариантах перезапуск функций


def funct_sort(filter_state_list_trans: dict) -> dict:
    # print("Отсортировать операции по дате? Да/Нет")
    s_data = str(input("Отсортировать операции по дате? Да/Нет")).lower()
    if s_data == "да":
        s_upp = str(input("Отсортировать по возрастанию или по убыванию?")).lower()
        if s_upp == "по возрастанию":
            return filter_state_list_trans["data"].sort  # возвращаут список отсортированный по дате возрастания
        elif s_upp == "по возрастанию":
            return filter_state_list_trans["data"].sort(reverse=True)  # возвращаут список отсортированный по дате
        # убывания
        else:
            return filter_state_list_trans  # возвращаут не отсортированный список

    else:
        return filter_state_list_trans  # возвращает не измененный список


def rub_sort(filter_state_list_trans: dict) -> dict:
    s_rub = str(input("Выводить только рублевые тразакции? Да/Нет")).lower()
    filter_state_list_trans_ = []
    if s_rub == "да":
        for [currency_code] in filter_state_list_trans:
            if [currency_code] == "RUB":
                filter_state_list_trans_rub = filter_state_list_trans["currency_code"]
                filter_state_list_trans_ = filter_state_list_trans_rub
        return filter_state_list_trans_
    else:
        filter_state_list_trans_ = filter_state_list_trans
        return filter_state_list_trans_


def str_sort(filter_state_list_trans_: dict) -> dict:
    sort_string: bool = False
    s_string = str(input("""Отфильтровать список транзакций по определенному слову
в описании? Да/Нет""")).lower()
    if s_string == "да":
        return sort_string
    else:
        return sort_string
