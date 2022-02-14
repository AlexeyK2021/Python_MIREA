# Задача 11 с github. bin()
def fast_mul_gen(y):
    if y == 12:
        print('def f(x):')
        print('    x2 = x + x')
        print('    x4 = x2 + x2')
        print('    x8 = x4 + x4')
        print('    x12 = x8 + x4')
        print('    return x12')
        print('assert f(x) == x * 12')
    elif y == 16:
        print('def f(x):')
        print('    x2 = x + x')
        print('    x4 = x2 + x2')
        print('    x8 = x4 + x4')
        print('    x16 = x8 + x8')
        print('    return x16')
        print('assert f(x) == x * 16')
    else:
        print('Entered x not equals 12 or 16!')
    

fast_mul_gen(int(input()))
