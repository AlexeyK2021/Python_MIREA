from math import *


def main(x, z):
    f = sqrt((((17 * z ** 3 + 91 * x) ** 6) / 59 + 72 * x ** 4) /
             (abs(z ** 3 + 33 * x + 1) + z ** 5)) + \
        ((54 * (((z ** 2) / 86) - 77) ** 4 + 50 *
          (0.01 + x ** 2 + z ** 3) ** 6) /
         ((51 * exp(83 * (z ** 2) + z + 1) ** 2) - atan(x) ** 3))
    return f


if __name__ == "__main__":
    print(main(0.63, -0.3))
    print(main(-0.25, -0.34))
