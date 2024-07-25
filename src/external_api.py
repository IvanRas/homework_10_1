import os

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")


def convert_from_i_to_rub(transaction: dict[str, float]) -> float | str:
    """Функция принимает значение в долларах, обращается к API и возвращает конвертацию в рубли/"""
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        return amount
    elif currency == "USD":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        headers = {"apikey": api_key}
        response = requests.request("GET", url, headers=headers)
        json_result = response.json()
        rub_amount = json_result["result"]
        return rub_amount
    elif currency == "EUR":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        headers = {"apikey": api_key}
        response = requests.request("GET", url, headers=headers)
        json_result = response.json()
        rub_amount = json_result["result"]
        return rub_amount
    else:
        return "Неизвесная волюта"
        # говорит о возрощений пипа str, ошибка из за того то не float


#rub_operation = {"operationAmount": {
#   "amount": "123.45",
#    "currency": {
#        "code": "RUB"}}}

#usd_operation = {"operationAmount": {
#   "amount": "2.0",
#    "currency": {
#       "code": "USD"}}}

#eur_operation = {"operationAmount": {
#    "amount": "3.58",
#    "currency": {
#       "code": "EUR"}}}
#
#e_operation = {"operationAmount": {
#    "amount": "3.58",
#    "currency": {
#       "code": "FRN"}}}
#
#print(convert_from_i_to_rub(rub_operation))  # должно вернуться конкретно 123.45
# следующие запрос могут вернуть сумму чуть больше\меньше, в зависимости от курсов валют
#print(convert_from_i_to_rub(usd_operation))  # должно вернуться примерно 174.62
#print(convert_from_i_to_rub(eur_operation))  # должно вернуться примерно 341.74
#print(convert_from_i_to_rub(e_operation))
