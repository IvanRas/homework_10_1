import os
from typing import Any


import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")


def convert_from_usd_to_rub(amount: float) -> Any:
    """Функция принимает значение в долларах, обращается к API и возвращает конвертацию в рубли/"""
    # amount == operations["operationAmount"]["currency"]["code": "RUB"]
    if amount == ["operationAmount"]["currency"]["code": "RUB"]:
        return amount
    elif amount == ["operationAmount"]["currency"]["code": "USD"]:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=rub&from=USD&amount={amount}"
        headers = {"apikey": api_key}
        response = requests.request("GET", url, headers=headers)
        result = response.text
        return result
    else:
        return "Неизвесная волюта"
