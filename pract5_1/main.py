
def calculate(expr):
    '''
    Вычисление выражения в виде строки (Только одно действие).
    >>> calculate("1 + 1")
    2
    >>> calculate("5 * 4")
    20
    >>> calculate("2 / 2")
    1.0
    >>> calculate("5 - 7")
    -2
    >>> calculate("5 / 0")
    'Деление на ноль'
    '''

    num1 = 0
    num2 = 0
    action = ""
    for i in range(len(expr)):
        if expr[i] == "+" or expr[i] == "-" or expr[i] == "*" or expr[i] == "/":
            action = expr[i]
            num1 = expr[0:i]
            num2 = expr[i + 1:]
    if action == "+":
        return int(num1) + int(num2)
    elif action == "-":
        return int(num1) - int(num2)
    elif action == "*":
        return int(num1) * int(num2)
    elif action == "/":
        if int(num2) == 0:
            return "Деление на ноль"
        return int(num1) / int(num2)


if __name__ == "__main__":
    print(calculate(input()))
