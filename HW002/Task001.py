# На столе лежат n монеток.
# Некоторые из них лежат вверх решкой,
# а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# *Пример:
# 5 -> 1 0 1 1 0
# 2
# *

from random import randint

count_tails = 0
count_eagle = 0
number_coin = int(input('Введите кол-во монет: '))
for _ in range(1, number_coin + 1):
    coin = randint(0, 1)
    print(f'сторона -> {coin}')
    if coin == 0:
        count_tails += 1
    else:
        count_eagle += 1
if count_tails>count_eagle:
    print(f'Необходимо перевернуть {count_eagle}')
else:
    print(f'Необходимо перевернуть {count_tails}')