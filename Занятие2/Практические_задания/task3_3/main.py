def counter(fn):
    count = 0

    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)

        nonlocal count
        count += 1
        print(f"Функция {fn} вызвана {count} раз(а)")
        return result

    return wrapper


@counter
def some_func():
    pass


@counter
def other_func():
    pass


if __name__ == "__main__":
    some_func()
    some_func()

    other_func()
