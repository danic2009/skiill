# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# point = sd.get_point(100, 100)
# sd.circle(center_position=point, radius=50)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей


# radius = 50
# for _ in range(3):
#     radius += 5
#     point = sd.get_point(100, 100)
#     sd.circle(center_position=point, radius=radius)
# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг

# def bobble(point, step):
#     radius = 50
#     for _ in range(3):
#         radius += step
#         sd.circle(center_position=point, radius=radius, width=2)
#
#
# point = sd.get_point(100, 100)
# bobble(point, 5)

# Нарисовать 10 пузырьков в ряд

# for x in range(100, 1001, 100):  # Взял ранже с шагом шара
#     point = sd.get_point(x, 100)  # Создал шар
#     sd.circle(center_position=point, radius=50)  # Вызвал шар
# Нарисовать три ряда по 10 пузырьков

# for y in range(100, 301, 100):  # Взял ранже с шагом шара по высоте у
#     for x in range(100, 1001, 100):  # Взял ранже с шагом шара
#         point = sd.get_point(x, y)  # Создал шар
#         sd.circle(center_position=point, radius=50)  # Вызвал шар
# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код
radius = 50
for _ in range(100):
    point = sd.random_point()
    color = sd.random_color()
    sd.circle(center_position=point, radius=50, color=color)
sd.pause()
