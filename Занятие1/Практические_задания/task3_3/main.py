def some_iterator():
    str_ = "Hello, World"

    str_iterator_1 = iter(str_)  # получаем один итератор от итерируемого объекта типа str
    str_iterator_2 = iter(str_)  # получаем один итератор от итерируемого объекта типа str

    for i in range(1, 6):  # печатаем первые несколько элементов первого итератора строки
        print(f"Значение {i} итератора str_iterator_1: {next(str_iterator_1)}")

    print("-" * 10)

    for i in range(1, len(str_) + 1):   # печатаем все элементы второго итератора строки
        print(f"Значение {i} итератора str_iterator_2: {next(str_iterator_2)}")

    print("-" * 10)

    for char in str_iterator_1:  # печатаем оставшиеся элементы первого итератора строки
        print(f"Оставшиеся значение итератора str_iterator_1: {char}")


if __name__ == "__main__":
    some_iterator()
