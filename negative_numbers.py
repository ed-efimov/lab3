#Подключаем модуль random для того, чтобы генерировать случайные числа
from random import randint


#Создаем переменную для счетчика отрицательных чисел
count = 0


#Генерируем список из 15 чисел в диапазоне от -10 до 10 включая оба числа
b = [randint(-10, 10) for i in range(15)]

#Считаем кол-во отрицательных чисел
for i in range(len(b)):
    if b[i] < 0:
        count += 1


#Выводим список B и Кол-во отрицательных чисел в списке B
print("Список B:", b)
print("Кол-во отрицательных чисел в списке B:", count)