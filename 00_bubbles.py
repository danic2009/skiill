# -*- coding: utf-8 -*-

import simple_draw as sd

# sd.resolution = (1200, 600)
# point = sd.get_point(100, 100)
# sd.circle(center_position=point, radius=50)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

sd.resolution = (1200, 600)
radius = 50
for _ in range(3):
    radius += 5
    point = sd.get_point(100, 100)
    sd.circle(center_position=point, radius=radius)
# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# TODO здесь ваш код

# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код

# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код

sd.pause()
