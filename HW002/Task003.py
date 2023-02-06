# Требуется вывести все целые степени двойки
# (т.е. числа вида 2k),
# не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

number = int(input('Введите натуральное число: '))
degree = 1
while degree < number:
    degree *= 2
    if degree > number:
        break
    else:
        print(degree)
