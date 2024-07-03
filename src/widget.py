from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_string: str) -> str | None:
    """функция общей маскировки карты и счета."""
    if "Счет" in input_string:
        return get_mask_account(input_string)
    else:
        return get_mask_card_number(input_string)
    return None


def get_date(input_string: str) -> str | None:
    """Фнкция преобразования даты"""
    data = input_string.split("Т")[0]
    formatted_date = f"{data[8:10]}.{data[5:7]}.{data[:4]}"
    return formatted_date
