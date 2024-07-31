import json
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s: %(filename)s: %(levelname)s: %(message)s",
    filename="../logs/utils.log",
    # filename="utils.log",
    filemode="w",
)
auth_logger = logging.getLogger('app.auth')
# logger = logging.getLogger(__name__)
# file_handler = logging.FileHandler('utils.log')
# logger.addHandler(file_handler)
# logger.setLevel(logging.INFO)


def get_transactions_dictionary(path: str) -> dict:
    """Принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        # with open(path, "r", "operations.json", encoding='utf-8') as operations:
        with open(path, "r", encoding='utf-8') as operations:
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
