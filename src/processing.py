def filter_transactions(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция принимает на вход список словарей и значение для ключа 'state' (по умолчанию EXECUTED).
    Возвращает новый список словарей, у которых ключ 'state' содержит переданное в функцию значение.
    """
    return [transaction for transaction in transactions if state.lower() == transaction["state"].lower()]


def sort_transactions(transactions: list[dict], reverse: bool = True) -> list[dict]:
    """
    Функция принимает на вход список словарей и возвращает новый список словарей, отсортированный
    по ключу 'date' (по умолчанию в порядке убывания даты, т.е. от новой к старой). Если нужен порядок по
    возрастанию (от старой к новой), то нужно указать второй параметр False.
    """
    return sorted(transactions, key=lambda transaction: transaction["date"], reverse=reverse)
