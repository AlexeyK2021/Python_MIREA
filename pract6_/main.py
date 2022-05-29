def num(n):
    def f():
        return n

    return f


def add(op1, op2):
    def f():
        return op1() + op2()

    return f


def mul(op1, op2):
    def f():
        return op1() * op2()

    return f


if __name__ == "__main__":
    expr = mul(num(4), num(5))
    print(expr())


# 4,5,7,9,10,12

# Самостоятельно 4, 7, 12
