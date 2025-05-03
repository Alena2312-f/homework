import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, mask_number",
    [
        ("7000792289606361", "7000 79** **** 06361"),
        ("7158300734726758", "7158 30** **** 26758"),
        ("6831982476737658", "6831 98** **** 37658"),
        ("8990922113665229", "8990 92** **** 65229"),
        ("5999414228426353", "5999 41** **** 26353"),
    ],
)
def test_mask_card_number(card_number: str, mask_number: str) -> None:
    """Функция передает строку с номером карты"""
    assert get_mask_card_number(card_number) == mask_number


@pytest.mark.parametrize(
    "acc_number, mask_bank_account",
    [
        ("73654108430135874305", "**4305"),
        ("64686473678894779589", "**9589"),
        ("35383033474447895560", "**5560"),
        ("73654108430135874305", "**4305"),
    ],
)
def test_mask_account(acc_number: str, mask_bank_account: str) -> None:
    """Функция передает строку с номером счета"""
    assert get_mask_account(acc_number) == mask_bank_account