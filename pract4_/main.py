class A():
    class_var = 10

    def __init__(self):
        self.var = 5


# №1

class HashTable:

    def __init__(self):
        self._data = [list() for i in range(1024)]
        self.length = 0

    def _index(self, key):
        return hash(key) % len(self._data)

    def contains(self, key):
        lst = self._data[self._index(key)]
        return self.key_in(key, lst) is not None

    def key_in(self, key, lst):
        for kv in lst:
            if kv[0] == key:
                return kv
        return None

    def add(self, key, value):
        lst = self._data[self._index(key)]
        kv = self.key_in(key, lst)

        if kv is not None:
            lst.remove(kv)
        lst.append((key, value))
        self.length += 1

    def delete(self, key):
        lst = self._data[self._index(key)]
        kv = self.key_in(key, lst)

        if kv is not None:
            lst.remove(kv)
        self.length -= 1

    def length(self):
        return self.length

    def get(self, key):
        lst = self._data[self._index(key)]
        return lst[0]


if __name__ == "__main__":
    print(*dir(A), sep='\n')
