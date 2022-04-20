if __name__ == "__main__":
    str_ = "1q2w3e4r5t6y"
    chars = [char for char in str_ if char.isalpha()]  # TODO переписать с помощью filter
    char = filter(str.isalpha, str_)
    print("".join(chars))
