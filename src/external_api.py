import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")


def convert_from_usd_to_rub(amount: float) -> Any:
    """Функция принимает значение в долларах, обращается к API и возвращает конвертацию в рубли/"""
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=rub&from=USD&amount={amount}"
    headers = {"apikey": api_key}
    response = requests.request("GET", url, headers=headers)

    status_code = response.status_code
    result = response.text
    return
