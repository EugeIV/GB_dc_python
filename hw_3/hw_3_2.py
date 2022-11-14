# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random
n = random.randint(2, 11)
list_n = [random.randint(1, 9) for _ in range(n)]
new_list_n = []

if n % 2 == 0:
    for i in range(n // 2):
        new_list_n.append(list_n[i] + list_n[n - 1 - i])
else:
    for i in range(n // 2):
        new_list_n.append(list_n[i] + list_n[n - 1 - i])
    new_list_n.append(list_n[n // 2] + list_n[n // 2])

print(f'{list_n} => {new_list_n}')
