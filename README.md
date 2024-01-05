# `📚 min-menu-maker 📚`
> Make menus easily, efficiently, and concisely!
> 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

# Currently Unstable.
Due to some issues, you cannot currently use `min-menu-maker` in your code. This file will be updated once the issue is resolved.

## Requirements
 - ![Python](https://cdn-icons-png.flaticon.com/16/5968/5968350.png) Python Version: 3.11 and up!

## ⬇ Installation ⬇
 Run **either** of the following command to install `min-menu-maker`
 ```
py -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-package-YOUR-USERNAME-HERE
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

[Source code](https://github.com/Fenrir0279/min-menu-maker/blob/main/tests.py)
```python
import bullets
from menus import Menu, Choice

def beans(pwd: int):
    if pwd == 279: print("Beans")
    else: print("Not beans")

menu = Menu([
    Choice("Say hi but diff lang omg op",
        Menu([
            Choice("German", print, "Hallo"),
            Choice("Russian", print, "Privyet"),
            Choice("Latin", print, "Salve")
        ], bullets.NUMERICAL())
    ),
    Choice("Say hello", print, "Hello!"),
    Choice("Bean 12", beans, 12),
    Choice("Bean 279", beans, 279),
], bullets.Bullets('xy', '.'), "Choose!!!")

menu()
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
