def task(numbers: list) -> int:
    gen_exp = (num ** 2 for num in numbers)
    return sum(gen_exp)


if __name__ == "__main__":
    list_numbers = [i for i in range(1, 11)]  # list(range(1, 11))
    print(task(list_numbers))
