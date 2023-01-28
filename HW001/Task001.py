# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input('Введите трехзначное числo: '))
summa = 0
if 99 < number < 1000:
    while number > 0:
        num = number % 10
        number //= 10
        summa += num
    else:
        print(summa)
else:
    print('"Введено число несоответствующие требованию задачи!"')
