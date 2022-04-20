OUTPUT_FILE = "output.txt"


def task():
    with open(OUTPUT_FILE, "w") as f:
        f.write(",".join(str(i ** 2) for i in range(1, 11)))
        f.write("\n")


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
