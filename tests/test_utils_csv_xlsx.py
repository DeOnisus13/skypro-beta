import os

import pandas as pd

from src.utils_csv_xlsx import read_data_csv_file, read_data_xlsx_file


def test_read_data_csv_file():
    # Создание временного .csv файла для проверки
    test_csv_content = "a;b;c\n1;2;3\n4;5;6"
    abs_path = os.path.abspath("..")
    test_csv_filename = os.path.join(abs_path, "data", "test_data.csv")
    with open(test_csv_filename, "w") as test_csv:
        test_csv.write(test_csv_content)

    # Тестирование функции
    result = read_data_csv_file(test_csv_filename)

    expected_result = pd.DataFrame({"a": [1, 4], "b": [2, 5], "c": [3, 6]})
    pd.testing.assert_frame_equal(result, expected_result)

    os.remove(test_csv_filename)


def test_read_data_csv_file_error():
    result = read_data_csv_file("no_file.csv")
    assert result is None


def test_read_data_xlsx_file():
    # Создание временного .xlsx файла для проверки
    test_xlsx_content = {"A": [1, 2, 3], "B": [4, 5, 6]}
    abs_path = os.path.abspath("..")
    test_xlsx_filename = os.path.join(abs_path, "data", "test_data.xlsx")
    test_dataframe = pd.DataFrame(test_xlsx_content)
    test_dataframe.to_excel(test_xlsx_filename, index=False)

    # Тестирование функции
    result = read_data_xlsx_file(test_xlsx_filename)

    expected_result = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    pd.testing.assert_frame_equal(result, expected_result)

    os.remove(test_xlsx_filename)


def test_read_data_xlsx_file_error():
    result = read_data_xlsx_file("no_file.xlsx")
    assert result is None
