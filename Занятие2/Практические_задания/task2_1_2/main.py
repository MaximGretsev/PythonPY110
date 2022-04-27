import traceback
from traceback import print_exc


def second_gen(input_):
    yield input_
    input_ += 1

    yield input_
    input_ += 1

    return input_

    yield input_  # данный yield никогда не будет выполнен
    input_ += 1


def plus_num(input_):
    a = input_ + 1
    print(a)


if __name__ == "__main__":
    my_second_gen = second_gen(10)

    print(next(my_second_gen))
    print(next(my_second_gen))

    try:
        print(next(my_second_gen))
    except StopIteration as e:
        print(type(e))
        print("Генератор закончился")
        # print(e)
        print_exc()
