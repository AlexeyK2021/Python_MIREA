class Num:
    def __init__(self, num):
        self.result = self.operation = num
        self.stack_oper = f"PUSH {self.result}\n"
