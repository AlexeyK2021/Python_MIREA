import enum


class MilliState(enum.Enum):
    STATE_A = 0
    STATE_B = 1
    STATE_C = 2
    STATE_D = 3
    STATE_E = 4
    STATE_F = 3
    STATE_G = 4
    STATE_H = 5


class Milli:
    state = MilliState.STATE_A

    def __init__(self, state):
        self.state = state

    def post(self):
        if self.state == MilliState.STATE_A:
            self.state = MilliState.STATE_B
            return 0
        elif self.state == MilliState.STATE_C:
            self.state = MilliState.STATE_F
            return 4
        elif self.state == MilliState.STATE_F:
            self.state = MilliState.STATE_G
            return 7
        else:
            raise KeyError

    def merge(self):
        if self.state == MilliState.STATE_B:
            self.state = MilliState.STATE_C
            return 1
        elif self.state == MilliState.STATE_G:
            self.state = MilliState.STATE_D
            return 9
        elif self.state == MilliState.STATE_H:
            self.state = MilliState.STATE_F
            return 10
        else:
            raise KeyError

    def align(self):
        if self.state == MilliState.STATE_B:
            self.state = MilliState.STATE_D
            return 2
        else:
            raise KeyError

    def stare(self):
        if self.state == MilliState.STATE_C:
            self.state = MilliState.STATE_D
            return 3
        elif self.state == MilliState.STATE_D:
            self.state = MilliState.STATE_E
            return 5
        elif self.state == MilliState.STATE_E:
            self.state = MilliState.STATE_F
            return 6
        elif self.state == MilliState.STATE_G:
            self.state = MilliState.STATE_H
            return 8
        elif self.state == MilliState.STATE_H:
            self.state = MilliState.STATE_A
            return 11
        else:
            raise KeyError


def main():
    return Milli(MilliState.STATE_A)
