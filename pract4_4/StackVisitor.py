class StackVisitor:
    def __init__(self):
        self.stack_oper = ""

    def visit(self, data):
        self.stack_oper = data.stack_oper

    def get_code(self):
        return self.stack_oper
