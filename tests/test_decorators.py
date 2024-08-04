from src.decorators import log


def test_log_to_console(capfd):
    @log()
    def func():
        return "test"

    func()
    captured = capfd.readouterr()
    assert "Function func called" in captured.out


def test_log_to_file():
    @log(filename="test_log.txt")
    def func():
        return "test"

    func()
    with open("test_log.txt", "r") as f:
        assert "Function func called" in f.read()
