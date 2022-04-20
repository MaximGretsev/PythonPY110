import time


def time_decorator(fn):
    print("Этот код будет выведен в момент декорирования функции")

    def wrapper(*args, **kwargs):
        print("Этот код будет выполняться перед каждым вызовом функции")

        # TODO зафиксировать время до начала выполнения функции
        result = fn(*args, **kwargs)
        # TODO зафиксировать время после выполнения

        print("Этот код будет выполняться после каждого вызова функции")
        return result
    return wrapper


# TODO задекорировать функцию
def pow_(a, n):
    return pow(a, n)


if __name__ == "__main__":
    print(pow_)
    print("=" * 25)

    print(pow_(5, 2))
    print("=" * 25)

    print(pow_(4, 4))
