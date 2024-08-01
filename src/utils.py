import csv
import json
import logging
from typing import Any

import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s: %(filename)s: %(levelname)s: %(message)s",
    filename="../logs/utils.log",
    # filename="utils.log",
    filemode="w",
)
auth_logger = logging.getLogger("app.auth")
# logger = logging.getLogger(__name__)
# file_handler = logging.FileHandler('utils.log')
# logger.addHandler(file_handler)
# logger.setLevel(logging.INFO)


def get_transactions_dictionary(path: str) -> dict | Any:
    """Принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        # with open(path, "r", "operations.json", encoding='utf-8') as operations:
        with open(path, "r", encoding="utf-8") as operations:
            try:
                auth_logger.info("Информация по счету")
                transactions_data = json.load(operations)
                return transactions_data
            except json.JSONDecodeError:
                transactions_data = []
                auth_logger.info("Информация по счету не удачно")
                return transactions_data
    except FileNotFoundError:
        transactions_data = []
        auth_logger.info("Файл поврежден")
        return transactions_data
        # говорит о возрощений пипа list


excel_data = pd.read_excel("transactions_excel.xlsx")


def get_transactions_dictionary_excel() -> dict:
    """Принимает путь до Excel-файла и возвращает список словарей с данными о финансовых транзакциях."""

    auth_logger.info("Информация по счету")
    reader = csv.reader(excel_data)
#    to_dict:  что это за вставка и каки на что она влияет
    list_trans = reader.to_dict(orient="records")
    return list_trans


wine_reviews = pd.read_csv("transactions.csv")


def get_transactions_dictionary_csv() -> dict | Any:
    """Принимает путь до CSV-файла и возвращает список словарей с данными о финансовых транзакциях."""
    auth_logger.info("Информация по счету")
    reader = csv.reader(wine_reviews)
#    to_dict:  что это за вставка и каки на что она влияет
    list_trans = reader.to_dict(orient="records")
    return list_trans
