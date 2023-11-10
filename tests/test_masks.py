from src.masks import get_account_mask, get_card_mask


def test_get_card_mask():
    assert get_card_mask("7000792289606361") == "7000 79** **** 6361"
    assert get_card_mask(7000792289606361) == "7000 79** **** 6361"


def test_get_account_mask():
    assert get_account_mask("73654108430135874305") == "**4305"
    assert get_account_mask(73654108430135874305) == "**4305"
