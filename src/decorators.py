from functools import wraps
from typing import Callable, Any

def log(filename: None=None) -> None:
    """Декоратор для логирования вызовов функции."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                pass


@log
def my_func():
    pass
