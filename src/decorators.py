def log(filename: None=None) -> None:
    """Декоратор для логирования вызовов функции."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            pass


@log
def my_func():
    pass
