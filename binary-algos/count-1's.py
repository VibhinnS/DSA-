def get_1s(number):
    if not isinstance(number, int) or number < 0:
        raise ValueError("Invalid Input")

    count = 0

    while number:
        number &= number - 1
        count += 1
    return count


if __name__ == "__main__":
    import doctest
    doctest.testmod()
