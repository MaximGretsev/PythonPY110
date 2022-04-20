import json


def task():
    filename = "input.json"
    with open(filename) as f:
        json_data = json.load(f)

    map_iterator = map(lambda item: item["score"] * item["weight"], json_data)
    return sum(map_iterator)


if __name__ == "__main__":
    result = task()
    print(f"{result:.3f}")
