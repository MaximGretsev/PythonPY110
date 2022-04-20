def task() -> list:
    temp_tuple = (0, 36.6, 100)
    # for i in temp_tuple:
    #     result = (i * 1.8) + 32
    #     print(f'Температура в Фаренгейтах {result}')
    return list(map(lambda x: (x * 1.8) + 32, temp_tuple))  # TODO  вернуть список температур по Фаренгейту


if __name__ == "__main__":
    print(task())
