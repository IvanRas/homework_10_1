from src.decorators import log


@log()
def test_func(): return "test"


def test_log_to_console(capfd):
    test_func()
    captured = capfd.readouterr()
    assert "Function test_func called" in captured.out


@log(filename="test_log.txt")
def test_func_with_file():
    return "test"


def test_log_to_file():
    test_func_with_file()

    with open("test_log.txt", 'r') as f:
        assert "Function test_func_with_file called" in f.read()
