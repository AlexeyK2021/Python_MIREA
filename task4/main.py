from math import log10


def main(n):
    if n == 0:
        return -0.37
    elif n == 1:
        return 0.81
    elif n >= 2:
        return main(n - 1) - log10(main(n - 2) ** 2) ** 2 / 40


if __name__ == '__main__':
    print(main(2))
    print(main(5))
