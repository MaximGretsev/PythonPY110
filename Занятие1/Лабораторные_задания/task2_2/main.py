def task() -> int:
    list_numbers = [8, -8, 5, 5, -4, -7, -1, -3, 4, 8, -8, -3, -3, 4, 5, -5, 1, -7, 3, -2]

    # return sum([num for num in list_numbers if num < 0])  # TODO заменить list comprehension на filter
    return sum(filter(lambda x: x < 0, list_numbers))

if __name__ == "__main__":
    print(task())
