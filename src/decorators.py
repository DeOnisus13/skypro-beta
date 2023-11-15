from datetime import datetime
from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Функция 'декоратор', которая выводит лог результата выполнения
    вызываемой функции в файл, если он указан, или в консоль.
    """

    def wrapper(function: Callable) -> Callable:
        @wraps(function)
        def inner(*args: Any, **kwargs: Any) -> Any:

            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            try:
                result = function(*args, **kwargs)
                log_message = f"{current_datetime} {function.__name__} OK\n"

            except Exception as error:
                log_message = (
                    f"{current_datetime} {function.__name__} error: {type(error).__name__}. Inputs: {args}, {kwargs}\n"
                )
                result = None

            if filename:
                with open(filename, "a") as file:
                    file.write(log_message)
            else:
                print(log_message)

            return result

        return inner

    return wrapper
