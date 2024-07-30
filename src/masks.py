import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s: %(filename)s: %(levelname)s: %(message)s",
    filename="../logs/masks.log",
    filemode="w",
)


def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера карты."""
    logging.info(f"Маска карты{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(macc_number: str) -> str:
    """Функция маскировки номера счета."""
    mask_account = "**" + macc_number[-4:]
    logging.info(f"Маска счета{mask_account}")
    return mask_account
