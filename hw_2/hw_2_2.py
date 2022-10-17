# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

n = int(input())
list_n = []
num = 1

for i in range(1, n + 1):
    num *= i
    list_n.append(num)

print(list_n)
