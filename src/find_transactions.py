import re
from collections import Counter


def search_operations(transactions: list[dict], search_str: str) -> list[dict]:
    """
    Функция принимает список словарей с данными о банковских операциях и строку поиска.
    Возвращает список словарей, у которых в описании есть данная строка
    """
    return [
        transaction
        for transaction in transactions
        if re.search(search_str.lower(), transaction["description"].lower())
    ]


def get_category_count(transactions: list[dict], category_dict: dict) -> dict:
    """
    Функция принимает список словарей с данными о банковских операциях и словарь с категориями операций.
    Возвращает словарь, где ключ - название категории, значение - количество операций в категории.
    """
    return dict(
        Counter(
            [
                transaction["description"]
                for transaction in transactions
                if transaction["description"] in category_dict.values()
            ]
        )
    )
