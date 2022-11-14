# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в
# файле file.txt в одной строке одно число.

n = int(input())
list_n = [i for i in range(-n, n+1)]

print(list_n)

f = open('file.txt', 'w')
while True:
    s = input('Запишите позицию для вычисления: ')
    if s == '':
        break
    elif int(s) > len(list_n)-1:
        while int(s) > len(list_n)-1:
            s = input(f'Введите число меньше {len(list_n)}: ')
    f.write(s + '\n')
f.close()

result = 1
f = open('file.txt', 'r')
for line in f:
    if line == '':
        break
    result *= list_n[int(line)]
f.close()
print(result)
