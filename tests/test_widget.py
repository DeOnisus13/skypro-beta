import pytest

from src.widget import card_acc_info_mask, modify_date


@pytest.fixture
def card():
    return "Visa Platinum 7000792289606361"


@pytest.fixture
def account():
    return "Счет 73654108430135874305"


@pytest.fixture
def date():
    return "2018-07-11T02:26:18.671407"


def test_card_info_mask(card):
    assert card_acc_info_mask(card) == "Visa Platinum 7000 79** **** 6361"


def test_acc_info_mask(account):
    assert card_acc_info_mask(account) == "Счет **4305"


def test_modify_date(date):
    assert modify_date(date) == "11.07.2018"
