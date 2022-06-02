def number(num, next):
    def d():
        return num, next

    return d


def create_array(num):
    return number(num, None)


def pair(el, list):
    list()[1] = number(el, None)


def first(list):
    lst = list()[1]
    while True:
        lst = lst()[1]
        if lst()[1] is None:
            return lst()[0]


def rest(list):
    return list()[0]


def make_list(*args, list):
    lst = list()
    for el in args:
        lst = pair(el, lst()[1])
    return lst


if __name__ == "__main__":
    list = create_array(1)
    list = pair(2, list)
    list = pair(3, list)
