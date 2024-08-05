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
                list_trans = json.load(operations)
                return list_trans
            except json.JSONDecodeError:
                list_trans = []
                auth_logger.info("Информация по счету не удачно")
                return list_trans
    except FileNotFoundError:
        list_trans = []
        auth_logger.info("Файл поврежден")
        return list_trans
        # говорит о возрощений пипа list


def get_transactions_dictionary_excel() -> dict:
    """Принимает путь до Excel-файла и возвращает список словарей с данными о финансовых транзакциях."""

    auth_logger.info("Информация по счету")
    reader = pd.read_excel("../data/transactions_excel.xlsx")
#    to_dict:  что это за вставка, и как и на что она влияет
    list_trans = reader.to_dict(orient="records")
    return list_trans


def get_transactions_dictionary_csv() -> dict | Any:
    """Принимает путь до CSV-файла и возвращает список словарей с данными о финансовых транзакциях."""
    auth_logger.info("Информация по счету")
    reader = csv.reader(wine_reviews)
#    to_dict:  что это за вставка, и как и на что она влияет
    list_trans = reader.to_dict(orient="records")
    return list_trans


if __name__ == "__main__":
    wine_reviews = pd.read_csv("transactions.csv")
    excel_data = pd.read_excel("transactions_excel.xlsx")
