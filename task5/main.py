from math import atan, ceil


def main(y, z, x):
    number = 0
    n = len(y)
    for i in range(1, n + 1):
        number += 3 * atan(z[n - ceil(i / 2)] ** 3
                           - 20 * y[n - ceil(i / 4)] ** 2
                           - 63 * x[n - i]) ** 2
    return 70 * number


if __name__ == '__main__':
    print(main([0.25, 0.83, -0.18, 0.54, 0.89],
               [0.57, 0.22, 0.17, 0.58, -0.56],
               [-0.13, 0.91, 0.48, -0.86, -0.35]))
    print(main([0.38, 0.23, -0.01, 0.24, 0.51],
               [-0.26, 0.03, -0.06, 0.39, 0.28],
               [0.02, -0.39, -0.4, -0.21, 0.24]))
