import json
import os.path

import pytest

from src.utils import get_amount_transaction_rub, get_check_json


@pytest.fixture
def good_json_file():
    test_data = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
    ]
    abs_path = os.path.abspath("..")
    file_path = os.path.join(abs_path, "data", "test_data.json")
    with open(file_path, "w", encoding="UTF-8") as file:
        json.dump(test_data, file)
    return file_path


@pytest.fixture
def delete_file():
    abs_path = os.path.abspath("..")
    filename = f"{abs_path}\\data\\test_data.json"
    if os.path.exists(filename):
        os.remove(filename)


def test_get_check_json(good_json_file):
    transactions = get_check_json(good_json_file)
    assert transactions[0]["id"] == 441945886
    assert transactions[1]["description"] == "Перевод организации"
    if os.path.exists(good_json_file):
        assert good_json_file == "F:\\SkyPro_projects_beta\\HW_1\\data\\test_data.json"


def test_test_get_check_json_empty(good_json_file):
    abs_path = os.path.abspath("..")
    empty_file_path = os.path.join(abs_path, "data", "test_data_empty.json")
    with open(empty_file_path, "w", encoding="UTF-8") as file:
        file.write("")
    transaction = get_check_json(empty_file_path)
    assert transaction == []


# def test_test_get_check_json_error(good_json_file):
#     abs_path = os.path.abspath("..")
#     error_file_path = os.path.join(abs_path, "data", "test_data_error.json")
#     with open(error_file_path, "w", encoding="utf-8") as file:
#         file.write("invalid json data")
#     with pytest.raises(json.JSONDecodeError):
#         get_check_json(error_file_path)


@pytest.fixture
def rub_transaction():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


@pytest.fixture
def usd_transaction():
    return {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }


def test_get_amount_transaction_rub(rub_transaction):
    result = get_amount_transaction_rub(rub_transaction)
    assert isinstance(result, float)
    assert result == 31957.58


def test_calculate_transactions_in_rubles_invalid_currency(usd_transaction):
    with pytest.raises(ValueError, match="Транзакция выполнена не в рублях. Укажите транзакцию в рублях"):
        get_amount_transaction_rub(usd_transaction)
