from enum import Enum


def closest_power(base: int, of: int) -> int:
    n = 0
    while base > 1:
        n += 1
        base //= of
    return n


class Bullets:
    def __init__(self, text: str, *, on_exhaust_columnize=True):
        self.text = text
        self.iter_text = iter(self.text)
        self.on_exhaust_columnize = on_exhaust_columnize
        self.__curr = 0
        self.__size = None

        self.items = self.iter_text

    def __iter__(self):
        try:
            while True:
                yield next(self.items)
        except (GeneratorExit, StopIteration):
            self.check_overflow()

    def get_index_by_item(self, item):
        r = 0
        for i, sitem in enumerate(self.items):
            if sitem == item:
                r = i
                break
        self.check_overflow()
        return r

    def check_overflow(self, power=None):
        power = power or self.power
        self.items = self.create_gen(power)
        self.iter_text = f"self.create_gen({power})"

    @property
    def power(self):
        return closest_power(self.__size, len(self.text))

    def set_size(self, size: int):
        self.__size = size
        if self.power > 1:
            self.check_overflow()
        return self

    def create_gen(self, width: int):
        items = [0] * width
        while True:
            yield "".join(self.text[i] for i in items)
            items[-1] += 1
            items = self.check_overlap(items)
            if isinstance(items, Exception):
                raise items

    def __contains__(self, item):
        return item in self.text

    def check_overlap(self, items: list[int], max_size: int = None) -> list[int]:
        max_size = max_size or len(self.text)
        if any(i >= max_size for i in items):
            for ind, item in enumerate(items):
                if item >= max_size:
                    index = ind
            if index == 0:
                return ValueError("No text to proceed to!")
            items[index - 1] += 1
            items[index] = 0
            items = self.check_overlap(items, max_size)
        return items


class BulletType:
    letters_lower = Bullets("abcdefghijklmnopqrstuvwxyz")
    letters_upper = Bullets("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers_natural = Bullets("123456789")
    numbers_whole = Bullets("0123456789")


class BracketedBullets:
    letters_lower = BulletType.letters_lower
    letters_upper = BulletType.letters_upper
    numbers_natural = BulletType.numbers_natural
    numbers_whole = BulletType.numbers_whole


class CustomBulletType(Bullets):
    def __init__(self, characters, *, on_exhaust_columnize=True):
        super().__init__(characters, on_exhaust_columnize=on_exhaust_columnize)
