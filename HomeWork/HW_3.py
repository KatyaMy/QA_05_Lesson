# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3

# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(my_list[-2])


# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'

# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# result = (filter(lambda x: isinstance(x, int),list_1))
# print(sum(result))
# print(list_1)
# print(sum(filter(lambda x: isinstance(x, int),list_1)))
# print([x for x in list_1 if isinstance(x, str) and 'a' in x])!!!!!!!!!!

""""" 3.3. Превратите лист ['cat', 'dog', 'horse, 'cow'] в кортеж"""""
# my_list_2 = ['cat', 'dog', 'hors', 'cow']
# my_list_2 = (tuple(my_list_2))
# print(tuple(my_list_2))
# # print(type(my_list_2))


"""" 3.4. Напишите программу, которая определяет, какая семья больше.
      1) Программа имеет два input() - например, family_1, family_2.
      2) Членов семьи нужно перечислить через запятую.
   Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')"""""

# family_1 = tuple(input("Enter Family_1: "))
# family_2 = tuple(input("Enter Family_2: "))
# if len(family_1) == len(family_2):
#     print('Equal')
# elif len(family_1) > len(family_2):
#     print('family_1')
# else:
#     print('family_2')


""""3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение"""""

# film = {
#     'title': 'Шерлок Холмс',
#     'director': 'Игорь Масленников',
#     'year': 1979,
#     'budget':'100000',
#     'main_actor': 'Василий Ливанов',
#     'slogan':'Гениально и непостяжимо',
#     }
# print(film.keys())
# print(film.values())
# print(film.items())

#
# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# print(sum(my_dictionary.values()))


# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
# num = set([1, 2, 3, 4, 5, 3, 2, 1])
# print(num)

# # 3.8. Даны два множества:
# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# #      - найдите значения, которые встречаются в обоих множествах
# print(set1.intersection(set1, set2))
# #      - найдите значения, которые не встречаются в обоих множествах
# print(set2.difference(set1))
# #      - проверьте являются ли эти множества подмножествами друг друга
# #  ли первое множество является подмножеством второго, программа должна выводить True, в остальных случаях - False.
# print(set1.issubset(set2))
# print(set2.issuperset(set1))
