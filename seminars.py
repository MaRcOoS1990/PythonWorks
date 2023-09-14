
#! Seminar 3

# my_list = [1, 1, 2, 4, 1, 4, 5]

# size = int(input('Введите размер :'))

# my_list = []

# for i in range(size):
#     my_list.append(input('Введите числа:'))

# my_set = set(my_list)

# print(*my_set)
# print(len(my_list))


# n = int(input('Введите длинну:'))
# k = int(input('Введите число сдвига:'))%n

# list_1 = [int(input('Введите число:')) for i in range(1, n+1)]
# print(list_1)

# list_2 = list_1[-k:]+list_1[:-k]
# print(list_2)


# library = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {
#     "VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

# res_set = set()

# for cur_dict in library:
#     for key in cur_dict:
#         res_set.add(cur_dict[key])
# print(res_set)

# for cur_dict in library:
#     print(cur_dict.keys())
#     print(cur_dict.values())
#     print(cur_dict.items())
#     for key in cur_dict:
#         res_set.add(cur_dict[key])
# print(res_set)


# for cur_dict in library:
#     res_set.update(cur_dict.values())
# print(res_set)


# num_lst = [0, -1, 5, 2, 3, 7, 10, 5, 9]
# count = 0

# for i in range(len(num_lst)-1):
#     if num_lst[i] < num_lst[i+1]:
#         count += 1

# print(count)

# res_list = [num_lst[i+1]
#             for i in range(len(num_lst)-1) if num_lst[i] < num_lst[i+1]]

# res_list2 = [num_lst[i+1]if num_lst[i] < num_lst[i+1]
#              else 0 for i in range(len(num_lst)-1)]

# print(res_list)

# print(res_list2)

# print(len(res_list))

# from random import randint

# list_ran = [randint(0, 50) for i in range(10)]
# print(list_ran)

# for i in range(len(list_ran)):
#     for j in range(len(list_ran)-1):
#         if list_ran[j] > list_ran[j+1]:
#             list_ran[j], list_ran[j+1] = list_ran[j+1], list_ran[j]
# print(list_ran)


# def quick_sort(list_random, start, end):
#     left = start
#     right = end
#     pivot = list_random[(start+right)//2]
#     while True:
#         while list_random[left] < pivot:
#             left += 1
#         while list_random[right] > pivot:
#             right -= 1
#         if left <= right:
#             if left < right:
#                 list_random[left], list_random[right] = list_random[right], list_random[left]
#             left += 1
#             right -= 1
#         if left > right:
#             break
#     if left < end:
#         quick_sort(list_random, left, end)
#     if right > start:
#         quick_sort(list_random, start, right)


# quick_sort(list_ran, 0, len(list_ran)-1)
# print(list_ran)


#! Seminar 4
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# new = 'a a a b c a a d c d d'.split()
# print(new)
# dict_1 = {}
# for letter in new:
#     if letter in dict_1:
#         dict_1[letter] += 1
#         print(letter+'_'+str(dict_1[letter]), end=' ')
#     else:
#         dict_1[letter] = 0
#         print(letter, end=' ')


# text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# text_lower = set(text.lower().split())
# print(len(text_lower))


# n = int(input())
# max_number = n
# while n != 0:
#     if max_number < n:
#         max_number = n
#     n = int(input())
# print(max_number)


# ! Семинар 5


# def fib(num_1):
#     if num_1 in [1, 2]:
#         return 1
#     return fib(num_1-1)+fib(num_1-2)
# print(fib(7))

# from random import *
# n = 5
# list_1 = [randint(1, 5) for _ in range(n)]
# min1 = min(list_1)
# max1 = max(list_1)

# def change(min2, max2, list_2):
#     for i in range(len(list_2)):
#         if list_2[i] == max2:
#             list_2[i] = min2
#     return list_2

# print(list_1)
# print(min1, max1)
# print(change(min1, max1, list_1))

# def is_number_simple(num: int) -> bool:
#     if num % 2 == 0 and num != 2:
#         return False

#     for i in range(3, int(num ** 0.5+1), 2):
#         if num % i == 0:
#             return False
#         return True


# n = int(input('Введите число: '))
# if is_number_simple(num=n):
#     print(f'Число {n} является простым')
# else:
#     print(f'Число {n} простым не является')


# n = int(input('Введите количество чисел: '))


# def print_num(n: int) -> bool:
#     if n == 0:
#         return ''
#     line = input('Введите число: ')
#     return print_num(n-1)+line

# print(print_num(n))


# ! seminar 6
import random

# n = random.randint(5, 10)
# m = random.randint(5, 10)

# list_1 = [random.randint(1, 10)for i in range(n)]
# list_2 = [random.randint(1, 10)for i in range(m)]

# print(n, list_1)
# print(m, list_2)

# list_3 = [num for num in list_1 if num not in list_2]

# print(list_3)

# n = random.randint(5, 10)
# list_1 = [random.randint(1, 10)for _ in range(n)]
# print(n, list_1)
# count = 0

# for i in range(1, n-1):
#     if list_1[i-1] < list_1[i] > list_1[i+1]:
#         count += 1
# print(count)

# n = randint(5, 10)
# list_1 = [randint(1, 10)for _ in range(n)]
# print(n, list_1)

# count = 0

# for i in range(n-1):
#     for j in range(i+1, n):
#         if list_1[j] == list_1[i]:
#             count += 1
# print(count)


# def sum_div(num: int):
#     s = 1
#     for div in range(2, int(num**0.5+1)):
#         if num % div == 0:
#             s += div+num//div
#     return s


# k = int(input('Введите число-->'))
# result = []
# for num1 in range(2, k):
#     num2 = sum_div(num1)
#     sum2 = sum_div(num2)
#     if num1 == sum2 and num1 != num2:
#         temp = (num1, num2)
#         temp_res = min(temp), max(temp)
#         if temp_res not in result:
#             result.append(temp_res)
# for tuple_i in result:
#     print(*tuple_i)
