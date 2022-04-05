from back import settings, take_from_bunch, get_bunches, is_gameover
from termcolor import cprint, colored

banch = input('Сколько кучек?')
size = input('Сколько камней?')
settings(max_bunch=int(banch), max_size=int(size))
user_number = 1
while True:
    cprint('Текущая позиция', color='green')
    cprint(get_bunches(), color='green')
    user_color = 'blue' if user_number == 1 else 'yellow'
    cprint('Ход игрока{}'.format(user_number), color=user_color)
    pos = input(colored('Откуда брать?', color=user_color))
    qua = input(colored('Сколько берем?', color=user_color))
    step_seccessed = take_from_bunch(position=int(pos), quantity=int(qua))
    if step_seccessed:
        user_number = 2 if user_number == 1 else 1
    else:
        cprint('Невозможный ход', color='red')
    if is_gameover():
        break


cprint('Выиграл игрок номер {}'.format(user_number), color=user_color)
