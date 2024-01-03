from typing import Callable
from bullets import Bullets


class Choice:
    def __init__(
        self,
        message: str,
        action: Callable,
        *args,
        **kwargs
    ) -> None:
        self.message = message
        self.action = action
        self.args = args
        self.kwargs = kwargs

    def __call__(self):
        return self.action(*self.args, **self.kwargs)

    def __str__(self) -> str:
        return self.message


class Menu:
    def __init__(
        self,
        choices: list[Choice],
        bulleting_type: Bullets,
        greeting: str = None,
        **kwargs
    ) -> None:
        self.greeting = greeting
        self.choices = choices
        self.bulleting = bulleting_type

        self.include_space = kwargs.get('include_space', True)
        self.input_message = kwargs.get('input_message', '>>> ')

    def __call__(self):
        if self.greeting:
            print(self.greeting)

        for bullet, choice in zip(self.bulleting, self.choices):
            print(f"{bullet}{' ' if self.include_space else ''}{choice}")
        choice = input(self.input_message)
        index = self.bulleting.convert(choice)
        print(index)
        self.choices[index]()

