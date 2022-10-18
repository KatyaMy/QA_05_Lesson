import math


# predict_age = (65, 60, 75, 55, 60, 63, 64, 45)
# result = [num * num for num in predict_age]
# plus = sum(filter(lambda x: isinstance(x, int),result))
# sqrl = math.sqrt(plus)
# t = sqrl / 2
# print(t)

# def predict_age(*args):
#     return math.sqrt(sum(x*x for x in args))//2
# print(predict_age(65, 60, 75, 55, 60, 63, 64, 45))

# print(sqr)
# print(d)


#
# def sum_digits(number):
#     return abs(number)
# print(sum_digits(99))
#
#
# def sum_digits(number):
#     return 0 if number == 0 else int(number % 10) + sum_digits(int(number / 10))
#
# print(sum_digits(15))def calculator(x,y,op):
# #     if op == '+':
# #         return x + y
# #     elif op == '-':
# #         return x - y
# #     elif op == '*':
# #         return x * y
# #     elif op == '/':
# #         return x / y
# #     else:
# #         return 'unknown value'
# # print(calculator(2,"3",'456'))
#

# test1 = 'TestTes-tTes  tTestTest!*&'
# print(len(test1))
# -------
# text1 = 'Pig latin is cool'
# def pig_it(text):
#     a = text[1:3] + text[0] + 'ay'
#     b = text[5:9] + text[4] + 'ay'
#     c = text[11:12] + text[10] + 'ay'
#     d = text[14:17] + text[13] + 'ay'
#     return a + ' ' + b + " " + c + ' ' + d

# a = (text1[1:3] + text1[0]+ 'ay')
# b = (text1[5:9] + text1[4] + 'ay')
# c = (text1[11:12] + text1[10] + 'ay')
# d = (text1[14:17] + text1[13] + 'ay')
# print(pig_it('Pig latin is cool'))
# print(a,b,c,d)

# num = int(input())
# digit3 = num % 10
# digit2 = (num // 10) % 10
# digit1 = num // 100
# print(digit1, digit2, digit3, sep=',')
# num = 12345
# a = num % 100 // 10
# b = num % 1000 // 100
# c = num // 10000
# d = num % 10
# e = num % 10000 // 1000
#
# print(c)
# print(e)
# print(b)
# print(a)
# print(d)