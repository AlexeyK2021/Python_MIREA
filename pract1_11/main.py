def fast_mul_gen(y):
    x2 = 'x2'
    x4 = 'x4'
    x8 = 'x8'
    x16 = 'x16'
    i = 0
    x = ' '

    print('\n')
    print(f"def f(x): #Умножение на {y}")
    if y >= 2:
        print("    x2 = x + x")
    if y >= 4:
        print("    x4 = x2 + x2")
    if y >= 8:
        print("    x8 = x4 + x4")
    if y >= 16:
        print("    x16 = x8 + x8")

    while y > 1:
        if y % 2 == 1 and i == 0:
            x += 'x'
        if y % 2 == 1 and i == 1:
            x += ' + ' + x2
        if y % 2 == 1 and i == 2:
            x += ' + ' + x4
        if y % 2 == 1 and i == 3:
            x += ' + ' + x8
        if y % 2 == 1 and i == 4:
            x += ' + ' + x16
        i += 1
        y = y // 2

    i += 1
    if i == 5:
        x += ' + ' + x16
    if i == 4:
        x += ' + ' + x8
    if i == 3:
        x += ' + ' + x4
    if i == 2:
        x += ' + ' + x2
    if i == 1:
        x += 'x'
    x = x.lstrip()
    x = x.lstrip('+')

    print("    return " + x)


if __name__ == '__main__':
    fast_mul_gen(1)
    fast_mul_gen(6)
    fast_mul_gen(7)
    fast_mul_gen(15)
    fast_mul_gen(18)
    fast_mul_gen(28)
    fast_mul_gen(31)
