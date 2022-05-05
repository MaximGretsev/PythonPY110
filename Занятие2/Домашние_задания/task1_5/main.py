import itertools
import string
from string import ascii_lowercase, ascii_uppercase, digits
import random


# TODO: Поспрашивать преподавателя за реализацию. Кажется не ок.

def gen(n: int):
    print('Ваш пароль: ', end='')
    cnt = 0
    while cnt < n:
        gen_up = (i for i in random.sample(ascii_uppercase, n))
        print(next(gen_up), end='')
        yield gen_up
        cnt += 1
        gen_low = (i for i in random.sample(ascii_lowercase, n))
        print(next(gen_low), end='')
        yield gen_low
        cnt += 1
        gen_dig = (i for i in random.sample(digits, n))
        print(next(gen_dig), end='')
        yield gen_dig
        cnt += 1



if __name__ == "__main__":
    # print(ascii_lowercase)
    # print(ascii_uppercase)
    # print(digits)

    iter_ = gen(8)
    for _ in range(8):
        next(iter_)