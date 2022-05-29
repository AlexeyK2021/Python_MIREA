def decor(func):
    def inner(*args):
        print("args: ", args)

        ret = func(*args)
        print("return data: ", ret)
        return ret

    return inner


#
# def test(x):
#     return x ** 2


# print(test(2))
# test = decor(test(2))
# print(test(2))

@decor
def test(x):
    return x ** 2


# print(test(2))


# Задача 6 ***********************************************************************************************

PERF = {}


def make_perf(pd):
    def perf(func):
        def d(*args):
            pd.setdefault(func.__name__, 0)
            pd[func.__name__] += 1
            return func(*args)

        return d

    return perf


# perf = make_perf(PERF)


@make_perf(PERF)
def fact(n):
    if n == 0:
        return 1
    else:
        return fact(n - 1) * n


@make_perf(PERF)
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(5))
print(fact(10))
print(PERF)

# ***************************************************
print((lambda x: (4, x))(lambda n, f: n * f(n - 1, f) if n != 0 else 1))
# print(fact(5, fact))

# Задача 11 ************************************************************



