import logging

from src.utils import get_transactions_dictionary, get_transactions_dictionary_excel, get_transactions_dictionary_csv


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s: %(filename)s: %(levelname)s: %(message)s",
    filename="../logs/main.log",
    filemode="w",
)


auth_logger = logging.getLogger("app.auth")


# выбор типа фаила для чтения
def maim():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями. ")
    print(f'''Выберите необходимый пункт меню:\n
    1. Получить информацию о транзакциях из JSON-файла\n
    2. Получить информацию о транзакциях из CSV-файла\n
    3. Получить информацию о транзакциях из XLSX-файла\n
    ''')
    i = int(input())
    if i == 1:
        auth_logger.info("Для обработки выбран JSON-файл.")
        return get_transactions_dictionary # возвращает list_trans
    elif i == 2:
        auth_logger.info("Для обработки выбран CSV-файла.")
        get_transactions_dictionary_csv()
        return "Для обработки выбран CSV-файла.",  # возвращает list_trans
    elif i == 3:
        auth_logger.info("Для обработки выбран XLSX-файла.")
        return get_transactions_dictionary_excel # возвращает list_trans
    else:
        auth_logger.info("Не выбран тип файла")
        return maim()
# должны получить список для работы со следующими функциями


# в выбраном типе фаила производится фильрация по столбцу\словврь state
# выббераем только те где state == filters
def filter_funct(list_trans: dict) -> dict:
    print("""Введите статус, по которому необходимо выполнить фильтрацию. 
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
    filters = str(input()).upper()
    filter_state_list_trans = []
    # фильтрация
    for [state] in list_trans:
        if filters == "EXECUTED":
            auth_logger.info("Фильтрация по статусу: EXECUTED")
            filter_state_list_trans.append()
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
            return filter_funct()
    return filter_state_list_trans # следующий функция работает с даным списком


def funct_sort(filter_state_list_trans: dict) -> dict:
    print("Отсортировать операции по дате? Да/Нет")
    s_data = str(input()).lower()
    if s_data == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        s_upp = str(input()).lower()
        if s_upp == "по возрастанию":
            return filter_state_list_trans["data"].sort  # возвращаут список отсортированый по дате возрастания
        else:
            return filter_state_list_trans["data"].sort(reverse=True)  # возвращаут список отсортированый по дате убывания
    else:
        return filter_state_list_trans  # возвращает не измененый список


def rub_sort(filter_state_list_trans: dict) -> dict:
    print("водить только рублевые тразакции? Да/Нет")
    s_rub = str(input()).lower()
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
    print("""Отфильтровать список транзакций по определенному слову 
в описании? Да/Нет""")
    s_string = str(input()).lower()
    if s_string == "да":
        return sort_string = True
        # ["operationAmount"]["currency"]["code"] == "RUB"
    else:
        return sort_string
