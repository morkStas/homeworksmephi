"""3) Напишите программу, которая заполняет массив из N элементов случайными
целыми числами в диапазоне [ A , B ] и определяет номера двух соседних элементов этого
массива, имеющих минимальную сумму. Если таких пар несколько, нужно вывести
номера элементов самой последней пары.
Входные данные:
Входная строка содержит три числа: границы диапазона случайных чисел A и B , а также
размер массива N . Все числа разделены пробелами. Гарантируется, что 0 < N ≤ 10000 .
Выходные данные:
В первой строке программа должна вывести N элементов построенного массива, разделив
их пробелами, а во второй строке – номера двух соседних элементов массива, имеющих
минимальную сумму.
Примеры:
входные данные:
10 20 10
выходные данные:
10 10 19 12 13 17 13 11 14 14
1 2"""

from random import randint


def fillarray(a, b, n):
    return [randint(int(a), int(b)) for _ in range(int(n))]


def findminsum(arr):
    idx = [1, 2]
    minsum = arr[0] + arr[1]
    for i in range(1, len(arr) - 1):
        if (arr[i] + arr[i + 1]) <= minsum:
            minsum = arr[i] + arr[i + 1]
            idx = [i + 1, i + 2]
    return idx


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
    minval = findminsum(array)
    print(*minval)
    break
