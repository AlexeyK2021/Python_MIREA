def func(a, b=2, *c, d=4, e=1, **f):
    pass


# * - принимает беск кол-во аргументов (кортеж)
# ** - принимает все что явно не указано
def F(*, e, f):
    pass


if __name__ == '__main__':
    F(e=5, f="s")