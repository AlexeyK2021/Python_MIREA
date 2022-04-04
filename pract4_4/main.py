from Add import Add
from CalcVisitor import CalcVisitor
from Mul import Mul
from Num import Num
from PrintVisitor import PrintVisitor
from StackVisitor import StackVisitor


def main():
    ast = Add(Num(7), Mul(Num(3), Num(2)))
    pv = PrintVisitor()
    cv = CalcVisitor()
    sv = StackVisitor()
    print(pv.visit(ast))
    print(cv.visit(ast))
    sv.visit(ast)
    print(sv.get_code())


if __name__ == "__main__":
    main()
