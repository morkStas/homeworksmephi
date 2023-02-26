"""2) Напишите программу, которая заполняет массив из N элементов случайными
целыми числами в диапазоне [ A , B ] и отделяет положительные элементы массива от
отрицательных: переставляет все положительные (в том же порядке) в начало массива, а
все отрицательные (в том же порядке) – в конец массива, все нулевые элементы должны
оказаться в середине массива.
Входные данные:
Входная строка содержит три числа: границы диапазона случайных чисел A и B , а также
размер массива N . Все числа разделены пробелами. Гарантируется, что 0 < N ≤ 10000 .
Выходные данные:
В первой строке программа должна вывести N элементов построенного массива, разделив
их пробелами.
Во второй строке программа должна вывести в одну строчку все элементы получившегося
массива, разделив их пробелами.
Примеры:
входные данные:
-2 3 6
выходные данные:
1 -1 2 -2 0 3
1 2 3 0 -1 -2"""

from random import randint


def fillarray(a, b, n):
    return [randint(int(a), int(b)) for _ in range(int(n))]


def positiveZeroNegative(arr):
    positives, negatives, zero = [], [], []
    for i in range(len(arr)):
        if arr[i] > 0: positives.append(arr[i])
        if arr[i] < 0: negatives.append(arr[i])
        if arr[i] == 0: zero.append(arr[i])
    return positives + zero + negatives


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
    antiarray = positiveZeroNegative(array)
    print(*antiarray)
    break
