def main(m, n, a, p):
    number = 0
    number1 = 1
    for c in range(1, a + 1):
        for j in range(1, n + 1):
            for k in range(1, m + 1):
                number += 48 * j ** 2 - \
                          86 * (95 * c ** 2 - 95 * k ** 3 - p) ** 6
        number1 *= number
        number = 0
    return number1


if __name__ == '__main__':
    print(main(6, 5, 3, 0.58))
    print(main(8, 8, 4, 0.7))
