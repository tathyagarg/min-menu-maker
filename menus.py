from __future__ import annotations
from typing import Callable
from menu_maker.bullet_types import *

def iterate_over_with(options, bullets):
    size = len(options)
    bullets = iter(bullets.set_size(size))
    options = iter(options)

    try:
        while True:
            yield (i := next(bullets), next(options))
    except (GeneratorExit, StopIteration):
        return

class Menu:
    def __init__(
        self,
        options: list[str],
        actions: list[Menu | MenuAction],
        greeting: str = None,
        bullets: BulletType = None
    ) -> None:
        if len(set(options)) != len(options):
            raise ValueError("Repeating bullets")

        self.options = options
        self.actions = actions
        self.greeting = greeting
        self.bullets = bullets

    def run(self, *, bullet=None):
        b = isinstance(bullet, BracketedBullets)
        bullet = bullet or (self.bullets or BulletType.numbers_natural)

        if self.greeting:
            print(self.greeting)
        choice = input(
            '\n'.join(f'{bullet}{")" if b else ""} -> {value}' for bullet, value in iterate_over_with(self.options, bullet)) +
            '\nYour choice: '
        )
        while choice not in bullet:
            print("Invalid!")
            choice = input(
                '\n'.join(f'{bullet}{")" if b else ""} -> {value}' for bullet, value in iterate_over_with(self.options, bullet)) +
                '\nYour choice: '
            )

        self.actions[bullet.get_index_by_item(choice)].run()

class MenuAction:
    def __init__(self, action: Callable, args=(), **kwargs):
        self.action = action
        self.args = args
        self.kwargs = kwargs

    def run(self):
        return self.action(*self.args, **self.kwargs)

