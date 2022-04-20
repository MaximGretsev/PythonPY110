def task() -> str:
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]

    return min(list_words, key=len)  # используй ключевую у функции min, по которой она долна определять минимальный элемент
    # min(iterable, *[, key, default])


if __name__ == "__main__":
    print(task())
