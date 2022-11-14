# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input('Введите число: '))
f_1 = 0
f_2 = 1
list_fib = [1, 0, 1]

for i in range(1, n):
    fib = f_2 + f_1
    if i % 2 == 0:
        list_fib.insert(0, fib)
    else:
        list_fib.insert(0, -fib)
    list_fib.append(fib)
    f_2, f_1 = fib, f_2

print(list_fib)
