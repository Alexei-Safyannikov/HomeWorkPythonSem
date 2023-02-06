# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = input('Введите трехзначное числo: ')
if number == int(number):
    print(type(number))

    summa = 0
    if 99 < number < 1000:
        while number > 0:
            num = number % 10
            number //= 10
            summa += num
        else:
            print(f'Сумма цифр трехзначного числа = {summa}')
    else:
        print('"Введено число несоответствующие требованию задачи!"')
else:
    print('Никита')
