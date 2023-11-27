import os.path
from typing import Any

import pandas as pd


def read_data_csv_file(csv_file: str) -> Any:
    """
    Функция для считывания .csv файла
    """
    abs_path = os.path.abspath("..")
    csv_file_path = os.path.join(abs_path, "data", csv_file)
    if csv_file.find(".csv") and os.path.exists(csv_file_path):
        return pd.read_csv(csv_file_path, delimiter=";", encoding="utf-8")


def read_data_xlsx_file(xlsx_file: str) -> Any:
    """
    Функция для считывания .xlsx файла
    """
    abs_path = os.path.abspath("..")
    xlsx_file_path = os.path.join(abs_path, "data", xlsx_file)
    if xlsx_file.find(".xlsx") and os.path.exists(xlsx_file_path):
        return pd.read_excel(xlsx_file_path)
