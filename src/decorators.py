from typing import Callable, Any


def log(filename: None = None) -> Callable[[Any], Callable[[tuple[Any, ...], dict[str, Any]], Any]]:
    """Декоратор для логирования вызовов функции."""

    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            # Логирование результата
            log_message = f"Function {func.__name__} called with {args} and {kwargs}. Result: {result}"
            if filename:
                with open(filename, "a") as f:
                    f.write(log_message + "\n")
            else:
                print(log_message)
            return result
        return wrapper
    return decorator
