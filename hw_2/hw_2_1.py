# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

n = input()
list_num = [*n]
total = 0

for i in list_num:
    if i.isdigit():
        total += int(i)

print(total)
