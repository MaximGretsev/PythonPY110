def positive_check(fn):
    def wrapper(arg):
        if arg > 0:
            result = fn(arg)
            print(f"Число положительное {result}")
        else:
            raise ValueError("Аргумент функции не является положительным числом")
        return result
    return wrapper


@positive_check
def some_func(num: int):
    num = num ** 2
    return num


if __name__ == "__main__":
    some_func(5)  # всё хорошо

    some_func(-5)  # должна быть вызвана ошибка ValueError
