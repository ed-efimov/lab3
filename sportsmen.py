#Вводим изначальное кол-во километров и минимальное кол-во необходиых для пробега за день километров
x, y = None, None
while x == None and y == None:
    while x == None:
        try:
            x = float(input("Введите изначальное кол-во километров: "))
        except ValueError:
            print("Вы ввели не число. Повторите попытку")
            continue
        if x <= 0:
            x = None
            ("Вы ввели неположительное число. Повторите попытку")

    while y == None:
        try:
            y = float(input("Введите минимальное кол-во необходиых для пробега за день километров: "))
        except ValueError:
            print("Вы ввели не число. Повторите попытку")
            continue
        if y <= 0:
            y = None
            ("Вы ввели неположительное число. Повторите попытку")

    if x > y:
        print("Вы ввели x больше y. Повторите попытку")
        x, y = None, None


#Создаем переменную для номера дня, когда спортсмен сможет пробежать минимальное кол-во необходиых за день километров
n = 1


#Находим номер дня
while x < y:
    x *= 1.1
    n += 1


#Выводим номер дня
print("Спортсмен сможет пробежать не менее", y, "километров за день на", n, "день")