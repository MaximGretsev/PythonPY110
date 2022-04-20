from traceback import print_exc


def list_iterator():
    list_ = [1, 2, 3]
    list_iter = iter(list_)

    print(type(list_iter))  # <class 'list_iterator'>
    print(f"Является ли объект итератором? {list_ is iter(list_)}")  # Итерируемый объект

    print(next(list_iter))
    print(next(list_iter))
    print(next(list_iter))

    try:
        print(next(list_iter))
    except StopIteration:  # как только элементы в последовательности закончатся будет вызвано исключение StopIteration
        print_exc()


if __name__ == "__main__":
    list_iterator()
