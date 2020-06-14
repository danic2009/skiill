# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код
sd.resolution = (1200, 600)


# radius = 50
# for _ in range(3):
#     radius += 3
#     sd.circle(center_position=point, radius=radius, width=2)
def bubble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2)


#
#
# point = sd.get_point(500, 500)
# bubble(point, 100)

# for x in range(100, 1001, 100):
#     point = sd.get_point(x, 100)
#     bubble(point, 5)
for y in range(100, 401, 100):
    for x in range(100, 1001, 100):
        point = sd.get_point(x, y)
        bubble(point, 5)

simple_draw.pause()
