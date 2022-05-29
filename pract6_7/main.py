PERF = {}


def memo(func):
    computed_nums = {}

    def d(args):
        if args in computed_nums.keys():
            return computed_nums[args]
        else:
            num = func(args)
            computed_nums[args] = num
            return num

    return d


def make_perf(pd):
    def perf(func):
        def d(*args):
            pd.setdefault(func.__name__, 0)
            pd[func.__name__] += 1
            return func(*args)

        return d

    return perf


@memo
@make_perf(PERF)
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fact(n - 1) * n


@memo
@make_perf(PERF)
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    print(fact(10))
    print(fib(27))
    print(PERF)
