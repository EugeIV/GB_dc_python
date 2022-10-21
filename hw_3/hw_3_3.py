# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

import random

list_n = [(round(random.uniform(0, 10), 2)) for _ in range(5)]
new_list_n = [(round(i % 1, 2)) for i in list_n]

print(f'{list_n} => {max(new_list_n) - min(new_list_n)}')
