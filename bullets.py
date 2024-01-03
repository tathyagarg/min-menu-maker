import string

class Radix:
    def __init__(self, charset: str | list[str], starting_index: int = 0) -> None:
        self.charset = charset
        self.length = len(charset)
        self.starting_index = starting_index

        self.string = self.charset[starting_index]
        self.int_representation = [starting_index]

    def __iter__(self):
        return self
    
    def __next__(self):
        text = self.string
        self.add()
        return text
    
    def add(self):
        if self.int_representation[-1] == self.length-1:
            return self.carry_over()
        return self.regular_add()
    
    def regular_add(self):
        self.string = self.string[:-1] + self.charset[self.int_representation[-1]+1]
        self.int_representation[-1] += 1
        return self

    def carry_over(self):
        carry_size = 0
        for ch in self.int_representation[::-1]:
            if ch == self.length-1: carry_size += 1
            else: break
        if carry_size == len(self.int_representation):
            size = len(self.int_representation)
            self.string = self.charset[self.starting_index] + (self.charset[0] * size)
            self.int_representation = [self.starting_index] + ([0] * size)
        else:
            self.string = self.string[:-carry_size-1] + (self.charset[self.int_representation[-carry_size-1]+1]) + (self.charset[0] * carry_size)
            self.int_representation = self.int_representation[:-carry_size-1] + [self.int_representation[-carry_size-1]+1] + ([0] * carry_size)
        return self

class Bullets:
    def __init__(self, charset: str | list[str], ending_char: str, starting_index: int = 0) -> None:
        self.charset = charset
        self.ending_char = ending_char

        self.radix = iter(Radix(charset, starting_index))

    def __iter__(self):
        return self
    
    def __next__(self) -> str:
        return next(self.radix) + self.ending_char

    def convert(self, value: str) -> int:
        if any([i not in self.charset for i in value]): return -1
        total = 0
        for i, char in enumerate(value[::-1]):
            total += (self.charset.index(char) + 1) * (self.radix.length ** i)
        return total - 1 - self.radix.starting_index
        
        
class NUMERICAL(Bullets):
    def __init__(self, ending_char: str = '.') -> None:
        super().__init__("0123456789", ending_char, 1)

class LOWERCASE(Bullets):
    def __init__(self, ending_char: str = '.') -> None:
        super().__init__(string.ascii_lowercase, ending_char, 0)

class UPPERCASE(Bullets):
    def __init__(self, ending_char: str = '.') -> None:
        super().__init__(string.ascii_uppercase, ending_char, 0)

