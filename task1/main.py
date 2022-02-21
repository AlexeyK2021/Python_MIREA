from math import sin, exp, acos


def main(y, z, x):
    return ((sin(y ** 3 + 98 * z) ** 7 / 57 - 79 *
             acos(0.04 - x ** 3 / 52) ** 6) / (38 * (
                    z ** 3 / 36 - 1 - x ** 2) ** 6 - y ** 4)) - \
           (72 - y / 29 - 62 * z ** 2) ** 4 + 49 * exp(x) ** 2


if __name__ == "__main__":
    print(main(-0.83, 0.41, -0.14))
    print(main(0.81, -0.91, -0.86))
