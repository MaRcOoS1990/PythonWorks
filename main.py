'''Задача 10
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть.
Пример:
5 -> 1 0 1 1 0
2 '''
from random import randint
n = int(input('Введите число монеток: '))

list_coins = []
for i in range(n):
    list_coins.append(randint(0, 1))
print(list_coins)
zero_size = list_coins.count(0)
if len(list_coins) - zero_size < zero_size:
    print(f'Нужно перевернуть {len(list_coins) - zerzero_sizeo} монеток')
else:
    print(f'Нужно перевернуть {zero_size} монеток')
