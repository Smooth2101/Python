# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
sd.resolution = (1000, 500)
# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код
startPoint = sd.get_point(50,50)
stopPoint = sd.get_point(350,450)
for x in range(50,400,50):
    for y in range(350,750,50):
        startPoint = sd.get_point(x,50)
        stopPoint = sd.get_point(y, 450)
        color = sd.random_color()
        sd.line(start_point=startPoint,end_point=stopPoint,color=color,width=3)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# point = sd.get_point(1000, 0)
# step = 300
# for _ in range(7):
#     step += 50
#     color = sd.random_color()
#     sd.circle(center_position=point, radius=step, color=color, width=50)
sd.pause()
