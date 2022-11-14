# not(X or Y or Z) = not X and not Y and not Z

x, y, z = int(input('Введите X: ')), int(input('Введите Y: ')), int(input('Введите Z: '))

if not(x or y or z) == (not x and not y and not z):
    print("Истинно")
else:
    print("Ложно")
