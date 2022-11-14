# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

import random
list_n = [random.randint(1, 10) for _ in range(7)]
total = 0
print(list_n)

for i in range(1, len(list_n)):
    if i % 2 != 0:
        total += list_n[i]

print(total)
