# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# Пример:
# 5 -> 1 0 1 1 0
# 2 '''
# from random import randint
# n = int(input('Введите число монеток: '))

# list_coins = []
# for i in range(n):
#     list_coins.append(randint(0, 1))
# print(list_coins)
# zero_size = list_coins.count(0)
# if len(list_coins) - zero_size < zero_size:
#     print(f'Нужно перевернуть {len(list_coins) - zero_size} монеток')
# else:
#     print(f'Нужно перевернуть {zero_size} монеток')


# Задача 12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# Пример:
# 4 4 -> 2 2
# 5 6 -> 2 3 '''
# s = int(input('Введите сумму чисел: '))
# p = int(input('Введите произведение чисел: '))
# a = 0
# for x in range(s):
#     for y in range(s):
#         if x + y == s and x * y == p:
#             a += 1
#             print(x, y)
# if a == 0:
#     print('Вы ввели не корректные данные!')

# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2**k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8'''
# num = int(input('Введите число N: '))
# count = 0
# res = 1
# while res < num+1:
#     print(res, end=' ')
#     count += 1
#     res = 2 ** count


# holodos = 'cfghjhjgklrfgghrtyh 34576568aghjn k34t566ot7ikgnjhk078'
# word = 'anton'
# begin = 0
# for letter_w in word:
#     for i_h in range(begin, len(holodos)):
#         if letter_w == holodos[i_h]:
#             begin = i_h
#             break
#         else:
#             print('антона здесь нет')
#             break
# else:
# print('здесь есть антон')


# from flask import Flask

# app = Flask(__name__)


# @app.route('/')
# def main():
#     return "<h1>Hello, world!</h1><br><a href='/index' >перейти на вторую страницу</a>"


# @app.route('/index/<x>/<y>')
# def index(x, y):
#     return f'Результат : {int(x)+ int(y)}'
#     # return 'Its my first project'


# if __name__ == '__main__':
#     app.run()
