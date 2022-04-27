from itertools import count


def task():
    num = 2 ** 0  # 1
    yield num

    for i in count(1, 1):
        yield 2 ** i



if __name__ == "__main__":
    numbers = task()

    for _ in range(11):
        print(next(numbers))
