# x = -1
# print("Hello")
#
# if x < 0:
#     print("Меньше нуля")
# print("Good bay")
# a, b = 10, 5
# if a > b:
#     print("a > b")
#
# if a > b and a >0:
#     print("Good")
#
# if (a >b) and (a > 0 or b < 1000):
#     print("good")
#
# if 5 < b and b < 10:
#     print("Good")

# if '34' > '123':
#     print("Good")
#
# if '123' > '12':
#     print("Good")
#
# if [1, 2] > [1, 1]:
#     print("Good")

# print("Hello")
#
# x = 38
# if x < 0:
#     print("Меньше нуля")
# else:
#     print("Больше нуля")
# print("Good bay")

# print("Hello")
#
# x = 38
# if x < 0:
#     print("Меньше нуля")
# elif x == 0:
#     print("Равно нулю")
# elif x == 1:
#     print("Равно еденице")
# else:
#     print("Больше нуля")
# print("Good bay")

# Цыкл while(до тех пор пока)
# print("Hello")
# i = 1
# while i < 10:
#     i = i * 2
#     print(i)
# print("Good bay")

# print("Hello")
# f1, f2 = 1, 1
# while f2 < 100000000000:
#     print(f2)
#     next_f2 = f1 + f2
#     next_f1 = f2
#     f1, f2 = next_f1, next_f2
# print("Good bay")
# my_pets = ['lion', 'dog', 'skunk', 'hamster', 'cat', 'monkey']
# i = -1
# while i < len(my_pets):
#     i += 1
#     if i == 2:
#         continue
#     pet = my_pets[i]
#     print('Проверяем', pet)
#     if pet == 'cat':
#         print('Ура, кот найден!')
#         break
# print('Good bay')

# print("Hello")
# f1, f2, count = 0, 1, 0
# while f2 < 1000000:
#     count +=1
#     if count > 27:
#         print("Итерация больше 27 - прерываюсь")
#         break
#     f1, f2 = f2, f1 + f2
#     if f2 < 1000:
#         continue
#     print(f2)
# else:
#     print("Было", count, "итераций")

# Цикл for
# элементы списка

# a, b = 1, 2
# (a, b) = (1, 2)
# for element in [(1, 2), (3, 4)]:
#     a, b = element[0], element[1]
#     print(a + b)
#
# for (a, b) in [(1, 2), (3, 4)]:
#     print(a + b)

# pair_list = [(1, 2), (3, 4), (5, 6)]
# for a, b in pair_list:
#     print(a + b)
# tripl_list = [(1, 2, 3), (4, 5, 6)]
# for a, b, c in tripl_list:
#     print(a, b, c)

# Полезные функции в цикле

# zoo_pets = [
#     'lion', 'skunk',
#     'elephant', 'horse',
# ]
# for i, animal in enumerate(zoo_pets):
#     print(i, animal)

# for i in range(100, 600, 50):
#     print(i)
# zoo_pets = [
#     'lion', 'skunk',
#     'elephant', 'horse',
# ]
# for animal in zoo_pets:
#     for char in animal:
#         print(char)
#     print(animal)

zoo_pets_mass = {
    'lion': 300,
    'skunk': 5,
    'elephant': 5000,
    'horse': 400,
}
total_mass = 0


# for animal in zoo_pets_mass:
#     print(animal, zoo_pets_mass[animal])
#     total_mass += zoo_pets_mass[animal]
# print('Общая масса животных', total_mass)
# for animal, mass in zoo_pets_mass.items():
#     print(animal, mass)
#     total_mass += mass
# print('Общий вес животных', total_mass)
# for mass in zoo_pets_mass.values():
#     print(mass)
#     total_mass += mass
# print('Общая масса', total_mass)
# def same_func():
#     print('Привет! Я функция')
#
# same_func()
# my_list = [3, 14, 15, 92, 6]
# for element in my_list:
#     same_func()

# def function_with_params(param):
#     print('Функцию вызвали с параметром', param)
#
#
# my_list = [3, 14, 15, 92, 6]
# for element in my_list:
#     print('Начало цикла')
#     function_with_params(param=element)
#     print('Конец цикла')

# def power(number, pow):
#     print('Функцию вызвали с параметрами', number, 'в степени', pow)
#     power_value = number ** pow
#     return power_value
#
#
# my_list = [3, 14, 15, 92, 6]
# for element in my_list:
#     result = power(element, 10)
#     print(result)

def my_function():
    """Не делает ничего, но документируем,
    Нет, правда, Эта функция ничего не делает.
    """
    pass

print(my_function.__doc__)