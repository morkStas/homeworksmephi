"""задача №1 Напишите программу, которая заполняет массив из N элементов случайными
целыми числами в диапазоне [ A , B ] и находит в массиве номера элементов, равных
минимальному.
Входные данные:
Входная строка содержит три числа: границы диапазона случайных чисел A и B , а также
размер массива N . Все числа разделены пробелами. Гарантируется, что 0 < N ≤ 10000 .
Выходные данные:
В первой строке программа должна вывести N элементов построенного массива, разделив
их пробелами.
Во второй строке программа должна вывести в одной строке номера элементов массива,
равных минимальному, разделив их пробелами."""

from random import randint


def fillarray(a, b, n):
    return [randint(int(a), int(b)) for _ in range(int(n))]


def printminindex(arr):
    minimal = min(arr)
    for i in range(1, len(arr) + 1):
        if arr[i - 1] == minimal:
            print(i)


def check(num):
    tupple = num.split()
    if len(tupple) != 3:
        for i in tupple:
            if not i.isdigit():
                print("Одно или несколько значений в строке не число или не верный ввод!")
                return True
        print("Hе верный ввод!")
        return True
    return False


while True:
    value = input("Введите числа A, B, N через пробел: ")
    if check(value): continue

    array = fillarray(*value.split())
    print(*array)
    printminindex(array)
    break
