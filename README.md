# `📚 min-menu-maker 📚`
> Make menus easily, efficiently, and concisely!
> 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Requirements
 - ![Python](https://cdn-icons-png.flaticon.com/16/5968/5968350.png) Python Version: 3.11 and up!

## ⬇ Installation ⬇
 Run **either** of the following command to install `min-menu-maker`
 ```
    pip install git+https://github.com/tathyagarg/min-menu-maker.git
    python -m pip install git+https://github.com/tathyagarg/min-menu-maker.git
 ```

## ✅ Features ✅
 What makes `min-menu-maker` special?
 * Amount of code requires is minimal (That's what the `min` stands for!), so fewer keystrokes.
 * You can customize what happens after a user selects an option by creating functions.
 * You can customize the text displayed before the user's options are presented, so the user knows what you're trying to ask.
 * You can customize the bullet points used to display the options.

 Of course, this isn't much. `min-menu-maker` wasn't originally made for 3rd party use, and instead because I was bored.
 However, I would still appreciate it if you would give it a try!

## 🤔 Usage example 🤔

Here's a simple example for `min-menu-maker`

[Source code](https://github.com/Fenrir0279/min-menu-maker/blob/main/tests/example.py) (comments added)
```python
from menu_maker.menus import Menu, MenuAction
from menu_maker.bullet_types import CustomBulletType


def big_action(text: str) -> None:
    """
    A lot of code can go here, to perform large pieces of code,
    after the corrosponding menu option is selected
    """
    a = input(text)
    print(f"You entered: {a}")


my_menu = Menu(
    # Your options and actions must corrospond with each other, 
    # so the first item of options corrosponds with the first item of actions
    options=["Say hi", "Say bye", "Ignore", "Big Action (Wow)!"],
    actions=[
        Menu(
            options=["Hello!", "Hi!", "???"],
            actions=[
                MenuAction(lambda: print("Hello!")), # Menu actions take in functions (callables)
                MenuAction(lambda: print("Hi!")),
                MenuAction(lambda: print("HELLO GAMER!")),
            ],
        ),
        MenuAction(action=(lambda: print("Bye!"))),
        # You can specify positional arguments in the args parameter
        # kwargs are passed in as though calling the target function
        MenuAction(action=print, args=("I", "am", "ignoring", "you"), sep="_"),
        MenuAction(big_action, args=("Write something: ",)),
    ],
    greeting="Welcome to my epic menu!",
)

# There are only 4 possible bullets. If there are more than 5 options,
# The bullets will wrap, for example:
# abab, abcd, abef, abgh, cdab, cdcd, cdef, cdgh, ...
my_bullets = CustomBulletType(["ab", "cd", "ef", "gh"])
my_menu.run(bullet=my_bullets)
```

## ❓ Why `min-menu-maker` ❓
 So you're making a text based RPG, and need menus to get prompts from the user.
 Here's your though process: 
 
 * You 🤔: It'll take a lot of code to make that work, so you'll have to put them in seperate files, so you don't get confused.
 * You 🤢: This adds code into your environment that isn't related to RPG.
 * You 😔: If you want to make more text-based games in the future you'll have to copy this code again, or re-write it
 * You 😊: You find `min-menu-maker` and learn how easy it can be to make menus, so easy that you could fit it in just 1 line! (But please don't do it in just one line)
 
## 📖 [License](https://github.com/Fenrir0279/min-menu-maker/blob/main/LICENSE.txt) 📖

Copyright (c) 2022 tathyagarg

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal ...
