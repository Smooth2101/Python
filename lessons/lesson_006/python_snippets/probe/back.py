from random import randint
_holder = []

def settings(max_bunch, max_size):
    global _holder
    _holder=[]
    for i in range(max_bunch):
        _holder.append(randint(1, max_size))


def take_from_bunch(position, quantity):
    if 1 <= position <= len(_holder):
        _holder[position-1] -= quantity
        return True
    else:
        return False

def get_bunches():
    return _holder


def is_gameover():
    return sum(_holder) ==0
