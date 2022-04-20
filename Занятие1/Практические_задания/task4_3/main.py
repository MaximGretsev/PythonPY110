from itertools import repeat


def task():
    my_floats = [
        4.356345,
        6.0934,
        3.245235,
        9.77545,
        2.164234234,
        8.884234235,
        4.575235346645
    ]

    return list(map(round, my_floats, repeat(3)))  # TODO заменить на repeat


if __name__ == "__main__":
    print(task())
