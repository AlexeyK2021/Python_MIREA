PERF = {}


def make_perf(pd):
    def perf(func):
        def d(*args):
            pd.setdefault(func.__name__, 0)
            pd[func.__name__] += 1
            return func(*args)

        return d

    return perf


def memo(func):
    counted_nums = {}

    def d(args):
        if args in counted_nums.keys():
            return counted_nums[args]
        else:
            number = func(args)
            counted_nums[args] = number
            return number

    return d


@memo
@make_perf(PERF)
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


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
