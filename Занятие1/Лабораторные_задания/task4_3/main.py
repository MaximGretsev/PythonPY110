import itertools
from itertools import repeat


def task():
    a = 10
    for num in itertools.repeat(a, 4):  # TODO повторить переменную a 4 раза
        print(num)


if __name__ == "__main__":
    task()
