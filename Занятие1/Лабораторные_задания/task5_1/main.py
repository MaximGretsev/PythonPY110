def task():
    numbers = [1, 2, 3, 4, 5]
    chars = ["a", "b", "c", "d", "e"]
    for number, char in zip(numbers, chars):  # TODO поэлементно объединить numbers и chars
        print(f"{number}-{char}")


if __name__ == "__main__":
    task()
