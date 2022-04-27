import itertools


def count(start_number: float = 1, step: float = 1):
    gen_num = (i for i in my_count)  # TODO написать функцию-генератор возвращающую целые числа

    print(gen_num)


if __name__ == "__main__":
    my_count = itertools.count(10, 0.5)
    for _ in range(10):
        print(next(my_count))
