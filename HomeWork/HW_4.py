""""4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа): 
     периметр квадрата, площадь квадрата и диагональ квадрата."""""
import functools

# def square(a):
#     P = a * 4
#     S = a * a
#     D = (a * 2) + (a * 2)
#     return P, S, D
# print(square(2))

"""""4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно 
     в формате аргумент: значение. Например:"""""
# a ='Ivan'
# b = 'Ax'
# c = 23
# d = 'QA'
# def about(name,last_name,age,position):
#     return f'Name: {name},\n last Name: {last_name},\n Age: {age},\n Position: {position}'
# print(about('Ivan','Ax',23,'QA'))
# print(about(a,b,c,d))

""""4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только 
     положительные числа"""""

my_list = [20, -3, 15, 2, -1, -21]
# print(list(filter(lambda x: x > 0, my_list)))

"""4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке """
l1 = list(filter(lambda x: x > 0, my_list))
# print(l1)
g = functools.reduce(lambda x,y: x * y, l1)
print(g)
""""4.5. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления. 
     Примените эти функции в качестве методов в другом файле."""""

