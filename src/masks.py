def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера карты."""
    return f'{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}'


def get_mask_account(macc_number: str) -> str | None:
    """Функция маскировки номера счета."""
    mask_account = macc_number[:5] + "**" + macc_number[-4:]
    return mask_account
