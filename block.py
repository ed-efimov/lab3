#Создаём переменные для размеров прямоугольного отверстия
a, b = None, None

#Вводим размеры прямоугольного отверстия
while a == None and b == None:
    print("Введите размеры прямоугольного отверстия: ")
    while a == None:
        try:
            a = float(input("A: "))
        except ValueError:
            print("Вы ввели не число. Повторите попытку")
            continue
        if a <= 0:
            a = None
            print("Вы ввели неположительное число. Повторите попытку")

    while b == None:
        try:
            b = float(input("B: "))
        except ValueError:
            print("Вы ввели не число. Повторите попытку")
            continue
        if b <= 0:
            b = None
            print("Вы ввели неположительное число. Повторите попытку")



#Создаём переменные для размеров кирпича
x, y, z = None, None, None

#Вводим размеры кирпича
while x == None and y == None and z == None:
    print("Введите размеры кирпича: ")
    while x == None:
        try:
            x = float(input("X: "))
        except ValueError:
            print("Вы ввели не число. Повторите попытку")
            continue
        if x <= 0:
            x = None
            print("Вы ввели неположительное число. Повторите попытку")

    while y == None:
        try:
            y = float(input("Y: "))
        except ValueError:
            print("Вы ввели не число. Повторите попытку")
            continue
        if y <= 0:
            y = None
            print("Вы ввели неположительное число. Повторите попытку")

    while z == None:
        try:
            z = float(input("Z: "))
        except ValueError:
            print("Вы ввели не число. Повторите попытку")
            continue
        if z <= 0:
            z = None
            print("Вы ввели неположительное число. Повторите попытку")


#Определяем, пройдет ли кирпич через отверстие
if ((a >= x) and (b >= y)) or ((a >= y) and (b >= x)) or ((a >= x) and (b >= z)) or ((a >= z) and (b >= x)) or ((a >= z) and (b >= y)) or ((a >= y) and (b >= z)):
    print("Пройдет")
else:
    print("Не пройдет")