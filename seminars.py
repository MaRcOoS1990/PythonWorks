
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
