from my_calc import *

print(f' Summa = : {add(2, 3)}')
print(f'Minus = : {minus(113, 33)}')
print(f'Total: {multi(23, 9)}')
print(f'Total: {devision(45, 7)}')
print(f'Total: {exp(23, 4)}')
print(f'Total: {r_of_dev(33, 2)}')


def tests():
    assert add(5, 8) == 13, f'Wrong number, actual result is {add(5, 8)}'
    assert minus(10, 6) == 60, f'Wrong number, actual result is {minus(113, 33)}'
    assert multi(10, 0) == "Can't divide by zero", "Shouldn't divide by zero"
    assert devision(85, 28) == 57, f'Wrong number, actual result is {multi(85, 28)}'
    assert exp(9, 4) == 1, f'Wrong number, actual result is '

tests()