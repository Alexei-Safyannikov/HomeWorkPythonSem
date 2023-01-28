# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый,
# т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no


summa_right = 0
summa_left = 0
number_ticket = int(input('Введите шестизначный номер билета: '))
ticket = number_ticket

if 99999 < number_ticket < 1000000:
    while 999 < number_ticket < 1000000:
        num = number_ticket % 10
        number_ticket //= 10
        summa_right += num

    while 0 < number_ticket < 1000:
        num = number_ticket % 10
        number_ticket //= 10
        summa_left += num

    if summa_right == summa_left:
        print(f'{ticket}--> Yes')
    else:
        print(f'{ticket}--> No')

elif number_ticket == 0:
    print('000000 --> Yes')

else:
    print('"Введено число не соответствующие требованию задачи,прочтите еще раз условие задачи!"')
