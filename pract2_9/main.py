import os

a = 1
b = 1
c = 300000  # проверено в Python 3.10
d = 300000
print(a is b, c is d)  # происходит кэширование чисел (питон до 256, pycharm- любое повторяющееся число)

a, b = 'py', 'py'
c = ''.join(['p', 'y'])
print(a is b, a == c, a is c)
print(id(a), id(b), id(c))  # a is b <==> id(a) == id(b)

print("\u00bb\u00ab\u301d\u275d\u0022")