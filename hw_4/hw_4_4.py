# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.

from random import randint
from sympy import symbols
from math import prod

k = int(input('Введите натуральную степень k: '))
koef = [randint(-100, 100) for i in range(k)] + [randint(1, 100)]
x = symbols('x')

with open('file.txt', 'w') as data:
    data.write(str(sum(map(prod, zip(koef, [x ** i for i in range(k + 1)])))) + ' = 0')
