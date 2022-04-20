def positive_check(fn):
    def wrapper(arg):
        # TODO написать проверку положительности аргумента arg

        result = fn(arg)
        return result

    return wrapper


# TODO задекорировать функцию
def some_func(num: int):
    ...


if __name__ == "__main__":
    some_func(5)  # всё хорошо

    some_func(-5)  # должна быть вызвана ошибка ValueError
