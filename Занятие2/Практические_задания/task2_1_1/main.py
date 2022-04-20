from traceback import print_exc


def first_gen(input_):
    yield input_
    input_ += 1


if __name__ == "__main__":
    my_first_gen = first_gen(5)
    print(next(my_first_gen))

    try:
        next(my_first_gen)
    except StopIteration:
        print("Генератор закончился")
        print_exc()
