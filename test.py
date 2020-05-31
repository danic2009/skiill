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

print("Hello")
f1, f2, count = 0, 1, 0
while f2 < 1000000:
    count +=1
    if count > 27:
        print("Итерация больше 27 - прерываюсь")
        break
    f1, f2 = f2, f1 + f2
    if f2 < 1000:
        continue
    print(f2)
else:
    print("Было", count, "итераций")
