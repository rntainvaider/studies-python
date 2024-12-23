"""Представьте: вы работаете со сторонним функционалом, который иногда возвращает неожиданный результат.

Ваша задача — создать декоратор retry_if_result_is_none для автоматического повторения функции N раз,
если результат функции не удовлетворяет заданному условию. Ваш декоратор должен иметь возможность
принимать аргумент times, который по умолчанию равен 1. Целевая функция, к которой будет применяться
результат, может вернуть либо какое-что значение, либо None.

И как только в одной из попыток «достучаться» до ответа функции — получении результата,
равного не None, — вы должны его вернуть.

Если получить хоть какое-то значение от функции не удалось за N раз, то вы должны вернуть None."""

import random


def retry_if_result_is_none(times=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                res = func(*args, **kwargs)
            return res

        return wrapper

    return decorator


@retry_if_result_is_none(times=2)
def test_function() -> None | str:
    return random.choice([None, "Passed"])


# Получилось получить значение за 2 вызова
print(test_function())
# Passed

# Не получилось получить значение за 2 вызова
print(test_function())
# None
