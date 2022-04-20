def task(words: list) -> list:
    return list(map(str.lower, words))


if __name__ == "__main__":
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]

    print(task(list_words))
