# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется
# жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний
# ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

import random

candies_total = 121
max_take_candies = 28
list_name = []
winner = ''
name_1 = list_name.append(input('Имя первого игрока: '))
name_2 = list_name.append(input('Имя второго игрока: '))
start = random.randint(0, 1)
print(start)
print(f'Первый ход делает: {list_name[start]}')

while candies_total > max_take_candies:
    player = list_name[start]
    candies = int(input(f'Игрок {player} введите количество конфет не более 28: '))
    while candies > max_take_candies:
        candies = int(input(f'Внимание {player} нужно ввести не более 28: '))
    candies_total -= candies
    print(candies_total)

    if candies_total > max_take_candies:
        player = list_name[abs(start - 1)]
        candies = int(input(f'Игрок {player} введите количество конфет не более 28: '))
        while candies > max_take_candies:
            candies = int(input(f'Внимание {player} нужно ввести не более 28: '))
        candies_total -= candies
        print(candies_total)
    elif candies_total <= max_take_candies:
        winner = list_name[abs(start - 1)]
    winner = list_name[start]

print(f'Победил {winner}')
