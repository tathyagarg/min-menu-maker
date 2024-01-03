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
