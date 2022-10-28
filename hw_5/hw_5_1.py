# Напишите программу, удаляющую из текста все слова, содержащие ""абв""

s = 'абв'
t = 'абфгд абвглда фабв абв а б в'


def del_string_from_text(text, string):
    new_text = ''.join(text.split(string))
    print(*new_text.split())


del_string_from_text(t, s)
