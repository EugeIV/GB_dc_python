# d = ((xA-xB)**2+(yA-yB)**2)**(1/2)

xA, yA = int(input('Введите координату X точки A: ')), int(input('Введите координату Y точки A: '))
xB, yB = int(input('Введите координату X точки B: ')), int(input('Введите координату Y точки B: '))

d = ((xA-xB)**2+(yA-yB)**2)**(1/2)
print(f'Расстояние между A и B: {round(d, 3)}')