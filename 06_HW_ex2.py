# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

my_list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 7
max_number = 10

# list_index = []
# i = 0
# for i in range(len(my_list)):
#     if my_list[i] >= min_number <= max_number:
#         list_index.append(i)
# print(list_index)

list_index = [i for i in range(len(my_list)) if min_number <= my_list[i] <= max_number]
print(list_index)



