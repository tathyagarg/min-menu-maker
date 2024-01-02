class Radix:
    def __init__(self, charset: str | list[str]) -> None:
        self.charset = charset
        self.length = len(charset)

        self.string = self.charset[0]
        self.int_representation = [0]

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
            self.string = self.charset[0] * (size + 1)
            self.int_representation = [0] * (size + 1)
        else:
            self.string = self.string[:-carry_size-1] + (self.charset[self.int_representation[-carry_size-1]+1]) + (self.charset[0] * carry_size)
            self.int_representation = self.int_representation[:-carry_size-1] + [self.int_representation[-carry_size-1]+1] + ([0] * carry_size)
        return self

class Bullets:
    def __init__(self, charset: str | list[str], ending_char: str, starting_index=0) -> None:
        self.charset = charset
        self.ending_char = ending_char
        self.power = None
        self.starting_index = starting_index
        self.items = iter(charset)

    def get_next_char(self) -> str:
        """
            Format of yield: overflow_character + character + ending character
            For example, with charset 'abc', ending character '.' and this being the 5th call, yield would be: 'ab.'
        """
        ...


# Predefined Bullets: TODO
