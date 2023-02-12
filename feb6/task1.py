"""1 Задача
С клавиатуры должны вводиться два целых числа a и b . Программа выводит сторону квадрата.
Например:
Входные данные:
Введите периметр a: 14
Введите периметр b: 16
Выходные данные:
Сторона квадрата: 5
Комментарии: при решении задачи необходимо использовать цикл либо while, либо for"""


def getside(a, b):
    return (a + b) / 6


def check(num):
    if not num.isdigit():
        print("Вы ввели не число.")
        return False
    return True


while True:
    perimeterA = input("Введите периметр a: ")
    if not check(perimeterA): continue
    perimeterB = input("Введите периметр b: ")
    if not check(perimeterB): continue
    print("Сторона квадрата:", getside(int(perimeterA), int(perimeterB)))
    break
