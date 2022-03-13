# -*- coding: utf-8 -*-
from random import random

import simple_draw as sd

sd.resolution = (1200, 600)
sd.background_color = (30, 147, 20)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(25, 550)
radius = 10
for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius)


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг

def bubble(point, step):
    radius = 20
    for _ in range(5):
        radius += step
        sd.circle(center_position=point, radius=radius)


step = 5
point = sd.get_point(100, 550)
bubble(point=point, step=step)
# Нарисовать 10 пузырьков в ряд

for x in range(100, 1200, 100):
    point = sd.get_point(x, 450)
    bubble(point=point, step=step)
# Нарисовать три ряда по 10 пузырьков
for x in range(100, 1200, 100):
    for y in range(100, 400, 100):
        point = sd.get_point(x, y)
        bubble(point=point, step=step)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):

    point=sd.random_point()
    color= sd.random_color()
    sd.circle(center_position=point,color=color)

sd.pause()
