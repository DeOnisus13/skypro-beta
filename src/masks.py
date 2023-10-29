def get_card_mask(card_number: int | str) -> str:
    """
    Функция создания маски номера карты
    :param card_number: Номер карты для маскировки
    :return: Маскированный по правилу номер карты
    """
    card_num_str = str(card_number)
    return f"{card_num_str[:4]} {card_num_str[4: 6]}** **** {card_num_str[-4:]}"


def get_account_mask(account_number: int | str) -> str:
    """
    Функция создания маски номера счета
    :param account_number: Номер счета для маскировки
    :return: Маскированный по правилу номер счета
    """
    return f"**{str(account_number)[-4:]}"
