from my_calc import *

print(f' Summa = : {add(2, 3)}')
print(f'Minus = : {minus(113, 33)}')
print(f'Total: {multi(23, 9)}')
print(f'Total: {devision(45, 7)}')
print(f'Total: {exp(23, 4)}')
print(f'Total: {r_of_dev(33, 2)}')


def tests():
    assert add(2, 3) == 5, f'Wrong number, actual result is {add(5, 8)}'
    assert minus(113, 33) == 80, f'Wrong number, actual result is {minus(113, 33)}'
    assert multi(23, 9) == 207, f'Wrong number, actual result is {multi(23, 9)}'
    assert devision(45, 7) == 6.4, f'Wrong number, actual result is {devision(45, 7)}'
    assert exp(23, 4) == 279841, f'Wrong number, actual result is {exp(23, 4)}'


tests()
