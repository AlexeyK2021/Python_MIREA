class Mul:
    def __init__(self, num1, num2):
        self.result = num1.result * num2.result
        self.operation = f"({num1.result} * {num2.result})"
        self.stack_oper = f"{num1.stack_oper}{num2.stack_oper}MUL\n"
