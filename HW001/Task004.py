# Требуется определить,
# можно ли от шоколадки размером n × m долек
# отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no
#

width_chocolate = int(input('Введите ширину шоколадки: '))
length_chocolate = int(input('Введите длину шоколадки: '))
numbers_slice = int(input('Введите кол-во долек шоколадки: '))
if numbers_slice % width_chocolate == 0 or numbers_slice % length_chocolate == 0:
    print('{} {} {} --> Yes'.format(width_chocolate, length_chocolate, numbers_slice))
else:
    print('{} {} {} --> No'.format(width_chocolate, length_chocolate, numbers_slice))
