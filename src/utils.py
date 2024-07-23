import json
from typing import Any

def get_transactions_dictionary():
    """Принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        with open('operations.json') as operations:
            transactions_data = json.loads(operations)
            return transactions_data
        except TypeError:
            transactions_data =[]
            return transactions_data
    except ValueError:
        transactions_data = []
        return transactions_data
