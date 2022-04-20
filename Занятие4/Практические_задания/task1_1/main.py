import re


def task():
    word_list = [
        ",./ sdfsdf",
        "Ddfsdf",
        "@@##,sdfsdf",
        "123_sdfsdf",
        "123sdfsdf",
        ", s,dfsdf",
        "123, fewfew",
    ]

    word_pattern = re.compile(...)  # TODO записать регулярное выражение для поиска слова любой длины

    for word in word_list:
        print(word_pattern)  # TODO вызвать от регулярного выражения методы search и group


if __name__ == "__main__":
    task()
