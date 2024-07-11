def log(filename: None = None) -> None:
    """Декоратор для логирования вызовов функции."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            # Логирование результата
            log_message = f"Function {func.__name__} called with {args} and {kwargs}. Result: {result}"
            if filename:
                with open(filename, 'a') as f:
                    f.write(log_message + '\n')
            else:
                print(log_message)
            return result
        return wrapper
    return decorator


@log
def my_func():
    pass
