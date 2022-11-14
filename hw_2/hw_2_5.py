# Реализуйте алгоритм перемешивания списка.

import random

list_n = [random.randint(0, 10) for i in range(random.randint(3, 30))]
print(f"исходный список: {list_n}")

random.shuffle(list_n)
print(f"список после перемешивания: {list_n}")
