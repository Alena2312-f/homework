import os

from src.logging import setup_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_1 = os.path.join(current_dir, "../logs", "masks.log")
logger = setup_logger("masks", file_path_1)


def get_mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты в формате - 7000792289606361,
    и возвращает ее маску 7000 79** **** 6361."""

    return card_number[:4] + " " + card_number[4:6] + "**" + " **** " + card_number[11:16]


print(get_mask_card_number(str()))


def get_mask_account(bank_account_number: str) -> str:
    """Принимает на вход номер счета в формате- 73654108430135874305 и
    возвращает его маску **4305."""

    return "**" + bank_account_number[-4:]


print(get_mask_account(str()))
