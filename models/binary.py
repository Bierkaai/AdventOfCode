class Bits:

    def __init__(self, int_val=None, bit_str=None, length=8):
        if int_val:
            self.int_repr = int_val
        elif bit_str:
            self.int_repr = self.parse_bitstr(bit_str)
        else:
            self.int_repr = 0
        self.length = length

    @classmethod
    def parse_bitstr(cls, bit_str):
        return int(bit_str, 2)

    def __int__(self):
        return self.int_repr

    def __str__(self):
        return format(self.int_repr, f'0{self.length}b')

    def __len__(self):
        return self.length

    def __invert__(self):
        inverted_val = ~int(self) & ((2 ** self.length) - 1)
        return Bits(int_val=inverted_val, length=self.length)

    @property
    def bit_count(self):
        return bin(int(self)).count("1")

    @property
    def most_common_bit(self):
        if self.bit_count > (self.length / 2):
            return 1
        else:
            return 0
