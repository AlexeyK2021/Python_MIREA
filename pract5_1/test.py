from main import calculate as calc


def test_1():
    assert calc("1 + 3") == 4


def test_2():
    assert calc("4 * 6") == 24


def test_3():
    assert calc("5 / 0") == 'Деление на ноль'


if __name__ == "__main__":
    pass
