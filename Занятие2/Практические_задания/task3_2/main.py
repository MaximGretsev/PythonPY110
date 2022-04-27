import time


def time_decorator(fn):
    print("Этот код будет выведен в момент декорирования функции")

    def wrapper(*args, **kwargs):
        print("Этот код будет выполняться перед каждым вызовом функции")

        t0 = time.time() # TODO Дома посмотреть этот модуль еще раз.
        result = fn(*args, **kwargs)
        dt = time.time() - t0 # TODO посмотреть этот подуль еще раз дома.
        print(f'Функция выполнилась за: {dt:.10f} фиг пойми чего')
        print("Этот код будет выполняться после каждого вызова функции")
        return result
    return wrapper


@time_decorator
def pow_(a, n):
    return pow(a, n)


if __name__ == "__main__":
    print(pow_)
    print("=" * 25)

    print(pow_(5, 2))
    print("=" * 25)

    print(pow_(4, 4))
