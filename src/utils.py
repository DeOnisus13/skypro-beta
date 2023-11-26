import json
import logging
import os.path
from typing import Any

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler("utils.log", mode="w", encoding="utf-8")

file_formatter = logging.Formatter("%(asctime)s - %(module)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def get_check_json(json_file_path: str) -> Any:
    """
    Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными.
    Если файл пустой, содержит не список или не найден, то возвращает пустой список.
    """
    try:
        abs_path = os.path.abspath("..")
        json_file_path_rep = json_file_path.replace("\\", "/")
        json_file_path_split = json_file_path_rep.split("/")
        json_file_path_join = os.path.join(abs_path, json_file_path_split[-2], json_file_path_split[-1])

        if os.path.exists(json_file_path_join):
            with open(json_file_path_join, encoding="utf-8") as file:
                logger.info("Функция отработала без ошибок")
                return json.load(file)
        else:
            print("Файла по указанному пути не существует")
            logger.warning("Файла по указанному пути не существует")
            return []

    except json.JSONDecodeError:
        print("Ошибка чтения файла")
        logger.error("Ошибка чтения файла")
        return []


def get_amount_transaction_rub(transaction: dict) -> float:
    """
    Функция принимает на вход одну транзакцию и возвращает сумму транзакции, если она совершена в рублях.
    Возвращает ошибку ValueError, если транзакция в другой валюте.
    """
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        logger.info("Данные получены успешно")
        return float(transaction["operationAmount"]["amount"])
    else:
        logger.warning("Указанная транзакция совершена не в рублях")
        raise ValueError("Транзакция выполнена не в рублях. Укажите транзакцию в рублях")
