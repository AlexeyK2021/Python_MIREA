import enum


class MilliState(enum.Enum):
    STATE_A = 0
    STATE_B = 1
    STATE_C = 2
    STATE_D = 3
    STATE_E = 4
    STATE_F = 5
    STATE_G = 6
    STATE_H = 7


class Milli:

    def __init__(self, state):
        self._state = state

    def post(self):
        if self._state == MilliState.STATE_A:
            self._state = MilliState.STATE_B
            return 0
        elif self._state == MilliState.STATE_C:
            self._state = MilliState.STATE_F
            return 4
        elif self._state == MilliState.STATE_F:
            self._state = MilliState.STATE_G
            return 7
        else:
            raise KeyError

    def merge(self):
        if self._state == MilliState.STATE_B:
            self._state = MilliState.STATE_C
            return 1
        elif self._state == MilliState.STATE_G:
            self._state = MilliState.STATE_D
            return 9
        elif self._state == MilliState.STATE_H:
            self._state = MilliState.STATE_F
            return 10
        else:
            raise KeyError

    def align(self):
        if self._state == MilliState.STATE_B:
            self._state = MilliState.STATE_D
            return 2
        else:
            raise KeyError

    def stare(self):
        if self._state == MilliState.STATE_C:
            self._state = MilliState.STATE_D
            return 3
        elif self._state == MilliState.STATE_D:
            self._state = MilliState.STATE_E
            return 5
        elif self._state == MilliState.STATE_E:
            self._state = MilliState.STATE_F
            return 6
        elif self._state == MilliState.STATE_G:
            self._state = MilliState.STATE_H
            return 8
        elif self._state == MilliState.STATE_H:
            self._state = MilliState.STATE_A
            return 11
        else:
            raise KeyError


def main():
    return Milli(MilliState.STATE_A)


if __name__ == "__main__":
    o = main()
    print(
        o.post(),  # 0
        o.merge(),  # 1
        o.stare(),  # 3
        o.stare(),  # 5
        o.post(),  # KeyError
        o.stare(),  # 6
        o.stare(),  # KeyError
        o.post(),  # 7
        o.stare(),  # 8
        o.merge(),  # 10
        o.merge(),  # KeyError
        o.post(),  # 7
        o.stare(),  # 8
        o.stare(),  # 11
        o.post(),  # 0
        o.merge(),  # 1
        o.post(),  # 4
        o.post(),  # 7
        o.merge(),  # 9
        sep="\n"
    )

# [0, 1, 3, 5, "<class 'KeyError'>", 6, "<class 'KeyError'>", 7, 6, "<class 'KeyError'>", 5, "<class 'KeyError'>", 6, 5, "<class 'KeyError'>", 9, 7, "<class 'KeyError'>", 9]
# 'post', 'merge', 'stare', 'stare', 'post', 'stare', 'merge', 'post', 'stare', 'merge', 'stare', 'post', 'stare', 'stare', 'post', 'merge', 'post', 'post', 'merge'
