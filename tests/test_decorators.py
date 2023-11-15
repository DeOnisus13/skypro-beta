import os.path
from datetime import datetime

import pytest

from src.decorators import log


@pytest.mark.parametrize(
    "x, y, expect", [(1, 2, "function OK"), (1, "2", "function error: TypeError. Inputs: (1, '2'), {}")]
)
def test_decorator_log_file(x, y, expect):
    filename = "test.txt"
    if os.path.exists(filename):
        os.remove(filename)

    @log(filename)
    def function(a, b):
        return a + b

    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    function(x, y)

    with open(filename) as file:
        log_message = file.read().strip()

    expect_log = current_datetime + " " + expect
    assert log_message == expect_log


@pytest.mark.parametrize(
    "x, y, expect", [(1, 2, "function OK"), (1, "2", "function error: TypeError. Inputs: (1, '2'), {}")]
)
def test_decorator_log_console(capsys, x, y, expect):
    @log()
    def function(a, b):
        return a + b

    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    function(x, y)

    console_message = capsys.readouterr()
    expect_log = current_datetime + " " + expect

    assert console_message.out.strip() == expect_log
