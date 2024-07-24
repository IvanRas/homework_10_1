import os


import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")


def convert_from_i_to_rub(amount: float, currency: str) -> float or str:
    """Функция принимает значение в долларах, обращается к API и возвращает конвертацию в рубли/"""
    # amount == operations["operationAmount"]["currency"]["code": "RUB"]
    # url = "https://api.apilayer.com/exchangerates_data/convert?to=to&from=from&amount=amount"
    if currency == ["operationAmount"]["currency"]["code": "RUB"]:
        return amount
    elif currency == ["operationAmount"]["currency"]["code": "USD"]:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        headers = {"apikey": api_key}
        response = requests.request("GET", url, headers=headers)
        result = response.text
        json_result = response.json()
        print(json_result)
        rub_amount = json_result["result"]
        print(json_result["result"])
        return rub_amount
    elif currency == ["operationAmount"]["currency"]["code": "EUR"]:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        headers = {"apikey": api_key}
        response = requests.request("GET", url, headers=headers)
        result = response.text
        json_result = response.json()
        print(json_result)
        rub_amount = json_result["result"]
        print(json_result["result"])
        return rub_amount
    else:
        return "Неизвесная волюта"
        # # говорит о возрощений пипа str, ошибка из за того то не float
