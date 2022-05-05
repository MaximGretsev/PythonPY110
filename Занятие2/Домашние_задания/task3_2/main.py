if __name__ == "__main__":
    def decorator(fn):

        def wrapper(arg1):
            if int(arg1):
                print('В аргументе число')
                result = fn(arg1)
            else:
                raise ValueError

            return result
        return wrapper

    @decorator
    def num(arg1):
        res = arg1 * 2
        return res


    print(num(4))