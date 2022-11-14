x, y = int(input('Введите X: ')), int(input('Введите Y: '))

if x != 0 and y != 0:
    if x > 0:
        if y > 0:
            print(1)
        elif y < 0:
            print(4)
    elif x < 0:
        if y > 0:
            print(2)
        elif y < 0:
            print(3)


else:
    print('Нулевые значения X и Y')
