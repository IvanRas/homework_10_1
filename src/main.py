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
    print('''Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла
    ''')
    i = int(input())
    if i == 1:
        auth_logger.info("Для обработки выбран JSON-файл.")
        return get_transactions_dictionary
    elif i == 2:
        auth_logger.info("Для обработки выбран CSV-файла.")
        return "Для обработки выбран CSV-файла.", get_transactions_dictionary_csv
    elif i == 3:
        auth_logger.info("Для обработки выбран XLSX-файла.")
        return get_transactions_dictionary_excel
    else:
        auth_logger.info("Не выбран тип файла")
        return maim()


# в выбраном типе фаила производится фильрация по столбцу\словврь state
# выббераем только те где state == filters
def filter_funct():
    print("""Введите статус, по которому необходимо выполнить фильтрацию. 
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
    filters = str(input()).upper()
    if filters == "EXECUTED":
        auth_logger.info("Фильтрация по статусу: EXECUTED")
        return get_transactions_dictionary
    elif filters == "CANCELED":
        auth_logger.info("Фильтрация по статусу: CANCELED")
        return get_transactions_dictionary_csv
    elif filters == "PENDING":
        auth_logger.info("Фильтрация по статусу: PENDING")
        return get_transactions_dictionary_excel
    else:
        auth_logger.info("Не выбран тип фильтрации")
        return filter_funct()


def funct_sort():
    sort_data: bool = False
    print("Отсортировать операции по дате? Да/Нет")
    s_data = str(input()).lower()
    if s_data == "да":
        return sort_data = True
    else:
        return sort_data


def upp_sort():
    sort_upp: bool = False
    print("Отсортировать по возрастанию или по убыванию?")
    s_upp = str(input()).lower()
    if sort_upp == "по возрастанию":
        return sort_upp = True
    else:
        return sort_upp


def rub_sort():
    sort_r: bool = False
    print("водить только рублевые тразакции? Да/Нет")
    s_rub = str(input()).lower()
    if sort_r == "да":
        return sort_r = True
        # ["operationAmount"]["currency"]["code"] == "RUB"
    else:
        return sort_r


def str_sort():
    sort_string: bool = False
    print("""Отфильтровать список транзакций по определенному слову 
в описании? Да/Нет""")
    s_string = str(input()).lower()
    if s_string == "да":
        return sort_string = True
        # ["operationAmount"]["currency"]["code"] == "RUB"
    else:
        return sort_string
