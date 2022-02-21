def main(z):
    if z < 49:
        return abs(z)
    elif 49 <= z < 113:
        return z ** 2 + (z ** 5) / 43
    elif 113 <= z < 192:
        return 85 * z ** 3 + ((1 + 34 * z ** 2) ** 7) / 62
    elif 192 <= z < 234:
        return 1 - (abs(z) ** 5)
    elif z >= 234:
        return 1 - (z ** 3 + 16 + 96 * z ** 2) ** 7


if __name__ == '__main__':
    print(main(61))
    print(main(251))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
