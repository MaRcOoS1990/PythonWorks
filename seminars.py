
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
