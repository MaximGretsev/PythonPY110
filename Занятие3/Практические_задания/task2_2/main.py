import json

OUTPUT_FILE = "output.json"
INPUT_FILE = "input.json"


def from_json_file():
    with open(INPUT_FILE) as f:
        python_object = json.load(f)
        return python_object


def to_json_file(python_object):
    with open(OUTPUT_FILE, "w") as f:
        json.dump(python_object, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    python_obj = from_json_file()
    print(python_obj)  # TODO распечатать объект как JSON строку с отступами и кодировкой

    to_json_file(python_obj)
