from itertools import count


def last_gen():
    for current_number in count(1):
        yield current_number
        if current_number == 5:
            return


if __name__ == "__main__":
    my_last_gen = last_gen()

    # for перехватывает ваше исключение
    for i in my_last_gen:
        print(i)
