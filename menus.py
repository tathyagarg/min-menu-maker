from typing import Any, Callable
from bullets import Bullets

# This whole file is basically one big TODO

class Choice:
    def __init__(
        self, 
        action: Callable
    ) -> None:
        self.action = action

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return self.action(*args, **kwargs)


class Menu:
    def __init__(
        self,
        greeting: str,
        choices: list[Choice],
        bulleting_type: Bullets
    ) -> None:
        pass

