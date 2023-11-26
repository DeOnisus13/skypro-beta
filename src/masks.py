import logging

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler("masks.log", mode="w", encoding="utf-8")

file_formatter = logging.Formatter("%(asctime)s - %(module)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def get_card_mask(card_number: int | str) -> str:
    """
    Функция создания маски номера карты
    :param card_number: Номер карты для маскировки
    :return: Маскированный по правилу номер карты
    """
    card_num_str = str(card_number)
    if len(card_num_str) == 16 and card_num_str.isdigit():
        logger.info(f"Номер карты {card_number} успешно замаскирован")
        return f"{card_num_str[:4]} {card_num_str[4: 6]}** **** {card_num_str[-4:]}"
    else:
        logger.error("Неверный номер карты для маскировки")
        return "Неверный номер карты для маскировки"


def get_account_mask(account_number: int | str) -> str:
    """
    Функция создания маски номера счета
    :param account_number: Номер счета для маскировки
    :return: Маскированный по правилу номер счета
    """
    account_number_str = str(account_number)
    if len(account_number_str) == 20 and account_number_str.isdigit():
        logger.info(f"Номер счета {account_number_str} успешно замаскирован")
        return f"**{str(account_number)[-4:]}"
    else:
        logger.error("Неверный номер счета для маскировки")
        return "Неверный номер счета для маскировки"
