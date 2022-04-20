def list_comprehension(words: list) -> list:
    return [str(item).capitalize() for item in words]  # TODO


def list_map(words: list) -> list:
    return list(map(str.capitalize, words))  # TODO


def task():
    list_words = [
        "goldenROD",
        "puRPle",
        "sAlMoN",
        "TURQUOISE",
        "cYAN"
    ]

    print(list_comprehension(list_words))
    print(list_map(list_words))


if __name__ == "__main__":
    task()
