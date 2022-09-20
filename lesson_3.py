# new_l = [x * x for x in l if x % 2]
# выражение x  в квадрате  для каждого x  в листе и если наш x  четный
# print(new_l)

# TUPLES()KoRTEJ
# mytuple = (23, 'true', 0, 'name')
# print(mytuple)
#
# letters = ('banana', 'apple', 'cat')
# a, b, c = letters
# print(a, b, c)

# letters[0] = 'ananas'
# print(letters) tuples ne izmenyemii

# для изменения кортеджа необходимо перевести в лист
# letters = list(letters)
# letters[0] = 'ananas'

# что бы поменять назад в кортедж
# print(tuple(letters))
#  *---- Getting index of items

# my_tuple = (1, 'True', 'name', None, 'Name', 'name', 90)

# print(my_tuple.index('name')) т.к  их несколько считет только индекс первого name
# print(my_tuple.count('name')) считает сколько всего name  в кортедже

# *--- Tuples method
# True = 1
# my_tuple = (1, True, 'name', None, 'Name', 'name', 32)
# result = tuple(filter(lambda x: isinstance(x, int),my_tuple))
# print(result)
#
# print(f'Sum is: {sum(result)}')
# print(f'Max is: {max(result)}')
# print(f'Min is: {min(result)}')
# print(f'Length of result : {len(result)}')
# print(f'Length of my_tuple: {len(my_tuple)}')

# *--- Получить индекс каждого значения
# my_tuple = (1, True, 'name', None, 'Name', 'name', 32)
# for(index, item) in enumerate(my_tuple):
#     print(index,item)

# *--- Iterate tuple with while loop
# my_tuple = (1, True, 'name', None, 'Name', 'name', 32)
# i = 0
# while i < len(my_tuple):
# # пока наш i меньше длины картежа, печатай наш элемент.
#     print(my_tuple[i])
#     i += 1

# *---- Nested list in tuple
#              0               1              2
#                         0         1       0        1
# letters = ('apple',['ananse', 'banana'], ['melon', 'mango'])
# letters[1][1] = 'orange'
# print(letters)
# print(letters[2][0])
# print(letters[-2])

# *--- swaping variables
# a = 5
# b = 10
# a, b = b,a
# print(a)
# print(b)

# *--- Passing tuple as an argument in function
# * это распаковка, идем по элементно по нашему кортежу
# def sum_it(*args):
#     total = 0
#     for num in args:
#         total = total + num
#     return total
# print(sum_it(4, 5, 10, 6, 20))


# def func(*args):
#     l = []
#     for item in args:
#         l.append(item * item)
#     return l
# print(func(4, 5, 10, 6, 20))

# **----DICTIONARY*---
# my_dict = {
#     'name': 'Anna',
#     'last name': 'Pavlova',
#     'age': 30,
#     'Department': 'IT'
# }
# print(my_dict)
# print(id(my_dict))
# print(my_dict['name'])
# my_dict['last name'] = 'Smirnova'
# print(len(my_dict))
# my_dict['salary'] = 5000
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
# print(my_dict.pop('salary'))
# print(my_dict)
# print(my_dict.get('name','Not found'))

# *---SET*---по индексам не проходится. Удаляет первое попавшееся значение.
# print(set([1, 2, 8, 5, 1, 8, 9]))
#
# set1 = {1, 2, 3, 'one', 'two'}
# set2 = {1, 2, 3, 'one', 'ten', 100, 525}
# set3 = {1, 2, 3}

# print(set1.issubset(set2))
#
# print(set2.issuperset(set1))
#пересечение множеств.повторение значений
# print(set2.intersection(set1, set3))
#
# # возвращает те значения которые различаются в сет1 и сет2(в скобках указывает то чье значение отличается от второго)
# print(set2.difference(set1))
# print(set1.difference(set2))
#
# print(set1.remove(1))
# print(set1.add(8))
# print(set1)

# fs = frozenset({1, 2, 3})
# print(fs)
#
# fs.remove(1)
# print(fs)
#
# fs.add(4)
# print(fs)
