#Подключаем модуль random для того, чтобы генерировать случайные числа
from random import randint


#Создаем переменную для кол-ва попыток, флага, чтобы определить отгадали ли код или нет и генерации кода
n = 0
flag = False
random_code = randint(100,999)

#Алгоритм для считывания кода и сверки его с заранее загаданым кодом. Если вводится 0, то код прерывается
while n < 5:
    code = None
    n += 1
    try:
        print("Введите код. Попытка №", n, ": ", end = "")
        code = int(input())
    except ValueError:
        print("Вы ввели не 3-значный код. Повторите попытку")
        n -= 1
        continue
    if code != 0 and (code < 100 or code > 999):
        code = None
        n -= 1
        print("Вы ввели не 3-значный код. Повторите попытку")
    if code == 0:
        print("Вы совершили принудительный выход из программы")
        break
    if code != None:
        if code == random_code:
            flag = True
            break


#Выводим результат
if flag == True:
    print("Код отгадан")
else:
    print("Попыток больше нет. Замок заблокирован")


#Сгенерированный код можно посмотреть при необходимости, убрав решетку в строке 39
#print("Сгенерированный код:", random_code)
