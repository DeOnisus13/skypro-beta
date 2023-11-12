from typing import Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Generator:
    """
    Функция принимает список словарей и возвращает итератор, который выдает по очереди операции,
    с указанной валютой.
    """
    filtered_transactions = filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions)
    for transaction in filtered_transactions:
        yield transaction


def transaction_descriptions(transactions: list[dict]) -> Generator:
    """
    Функция принимает список словарей и возвращает генератор с описанием каждой операции по очереди.
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start_number: int, end_number: int) -> Generator:
    """
    Функция генерирует номера банковских карт.
    """
    if len(str(start_number)) > 16 or len(str(end_number)) > 16 or start_number > end_number:
        yield "Неверные данные для генерации"
    for number in range(start_number, end_number + 1):
        start_of_num = "0" * (16 - len(str(number))) + str(number)
        yield f"{start_of_num[:4]} {start_of_num[4:8]} {start_of_num[8:12]} {start_of_num[12:]}"
