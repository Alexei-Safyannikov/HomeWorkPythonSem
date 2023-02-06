# Петя и Катя – брат и сестра.
# Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать.
# Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# *Пример:
# 4 4 -> 2 2
# 5 6 -> 2 *

summa = int(input('Введите сумму чисел: '))
composition = int(input('Введите произведение чисел: '))

number_one = 0
for i in range(10):
    number_one += 1
    number_two = 0
    for j in range(10):
        number_two += 1
        if summa == number_one + number_two and composition == number_one * number_two:
            print(f'Первое число -> {number_one}')
            print(f'Второе число -> {number_two}')
