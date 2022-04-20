def task(numbers: list) -> int:
    return sum(num ** 3 for num in numbers if num < 0)


if __name__ == "__main__":
    list_numbers = [-2, -1, 0, 1, -3, 2, -3]
    print(task(list_numbers))
