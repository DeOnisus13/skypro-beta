def filter_transactions(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция принимает на вход список словарей и значение для ключа 'state' (по умолчанию EXECUTED).
    Возвращает новый список словарей, у которых ключ 'state' содержит переданное в функцию значение.
    """
    return [transaction for transaction in transactions if state.lower() == transaction["state"].lower()]
