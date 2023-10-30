from src.masks import get_account_mask, get_card_mask


def card_acc_info_mask(card_acc_info: str) -> str:
    """
    Функция принимает на вход строку с информацией о типе карты/счета и номер карты/счета
    Возвращает эту строку с замаскированным номером карты/счета
    """
    card_acc_list = card_acc_info.strip().split()
    if card_acc_list[0] == "Счет":
        return f"{card_acc_list[0]} {get_account_mask(card_acc_list[1])}"
    else:
        return f'{" ".join(card_acc_list[:-1])} {get_card_mask(card_acc_list[-1])}'


def modify_date(date_raw: str) -> str:
    """
    Функция для изменения вывода даты
    :param date_raw: Дата для изменения
    :return: Отформатированная дата
    """
    date_list = date_raw.replace("T", " ").split()
    change_date_list = date_list[0].split("-")
    return ".".join(change_date_list[::-1])
