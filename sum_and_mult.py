#Создаём переменную для кол-ва введеных чисел
n = None

#Вводим кол-во чисел, которые введем, и проверяем его на то, чтобы оно было целым положительным числом
while n == None:
    try:
        n = int(input("Введите кол-во чисел: "))
    except ValueError:
        print("Вы ввели не целое число или вообще не число. Введите целое число")
        continue
    if n <= 0:
        n = None
        print("Вы ввели число меньше и равное нулю. Попробуйте ещё раз ввести кол-во чисел")


#Создаем переменную для суммы, произведения и счетчика цикла while
summa = 0
mult = 1
i = 0


#Вводим n чисел
while i < n:
    print("Введите", i+1, "- ое число: ", end = "")
    try:
        number = float(input())
    except ValueError:
        print("Вы ввели не число. Повторите попытку")
        continue
    summa += number
    mult *= number
    i += 1


if summa == int(summa):
    summa = int(summa)
if mult == int(mult):
    mult = int(mult)


#Выводим результат
if (n % 10 != 1) or (n % 100 == 11):
    print("Сумма", n, "введенных чисел:",summa)
    print("Произведение", n, "введенных чисел:",mult)
else:
    print("Сумма", n, "введенного числа:", summa)
    print("Произведение", n, "введенного числа:", mult)