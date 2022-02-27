def fast_mul(x, y):
    result = 0
    if x == 0 or y == 0:
        return 0

    while x // 2 != 0:
        y *= 2
        x //= 2
        if x % 2 == 1:
            result += y
    return result


def fast_mul_gen(y):
    pass
    # TODO it


if __name__ == "__main__":
    print(fast_mul(
        int(input("first number:")),
        int(input("second number:"))
    ))
