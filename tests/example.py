from menu_maker.menus import Menu, MenuAction
from menu_maker.bullet_types import CustomBulletType

def big_action(text: str) -> None:
    a = input(text)
    print(f'You entered: {a}')


my_menu = Menu(
    options=["Say hi", "Say bye", "Ignore", "Big Action (Wow)!"],
    actions=[
        Menu(
            options=["Hello!", "Hi!", "???"],
            actions=[
                MenuAction(lambda: print("Hello!")),
                MenuAction(lambda: print("Hi!")),
                MenuAction(lambda: print("HELLO GAMER!"))
            ]
        ),
        MenuAction(
            action=(lambda: print("Bye!"))
        ),
        MenuAction(action=print, args=("I", "am", "ignoring", "you"), sep='_'),
        MenuAction(big_action, args=("Write something: ",))
    ],
    greeting="Welcome to my epic menu!"
)

my_menu.run(bullet=CustomBulletType(['ab', 'cd', 'ef', 'gh']))
