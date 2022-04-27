def header_footer(fn):  # TODO написать декоратор

    def wrapper(*args):
        print("=" * 8)
        result = fn(*args)
        print("=" * 8)
        return result
    return wrapper


@header_footer
def my_func():
    print("Hello World")


if __name__ == "__main__":
    my_func()
