class WrapAroundInt(object):
    value: int
    wraparound: int
    initial_value: int

    def __init__(self, wraparound: int, initial_value: int = 1):
        self.wraparound = wraparound
        self.initial_value = initial_value
        self.value = initial_value

    def increment(self, i: int = 1) -> int:
        self.value = self.value + i
        if self.value > self.wraparound:
            self.value = self.value % self.wraparound
        return self.value

    def __add__(self, other) -> int:
        if isinstance(other, int):
            return self.increment(other)
        try:
            self.increment(int(other))
        except Exception:
            raise TypeError(f"{type(other)} could not be interpreted as int")

    def __int__(self):
        return self.value
