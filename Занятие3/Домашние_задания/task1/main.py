if __name__ == "__main__":
    first = 'first_file.txt'
    second = 'second_file.txt'
    with open(first) as f:
        with open(second) as k:
            res = zip(f, k)
            list_res = list(res)
            print(list_res)
            print(type(list_res))

            # TODO: Научиться прекидываться файл из ТХТ в JSON и в Pickle
    pass