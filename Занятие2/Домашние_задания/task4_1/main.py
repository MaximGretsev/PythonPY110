if __name__ == "__main__":
    pts = [
        (3, 4),
        (4.5, 3),
        (2.1, -1),
        (6.8, -3),
        (1.4, 2.9)
    ]
    #  TODO: Нифига не ясно. Спросить
    #
    # def get_distance(point: tuple) -> int:
    #     return (point[0] ** 2 + point[1] ** 2) ** 0.5
    #
    #
    # def task(points: list) -> list:
    #     return list(map(get_distance, points))
    #
    #
    # print(task(pts))

    def pairwise(iterable):
        for i in range(len(iterable) - 1):
            yield iterable[i] + iterable[i + 1]


    def task():
        for pair in pairwise(pts):
            print(pair)

    print(task())