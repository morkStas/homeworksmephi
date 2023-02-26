"""7) Напишите программу, которая генерирует массив из 100 случайных значений,
являющиеся значениями роста активистов в диапазоне [1500 , 2200 ], и определяет для
этого массива неудобство бригады, в которую объедены все 100 участников"""

from random import randint
import sys


def fillarray(a, b, n):
    return [randint(a, b) for _ in range(n)]


def maxdiff(arr):
    arr.sort()
    return max([arr[i + 1] - arr[i] for i in range(0, len(arr), 2)])


A, B, N = 1500, 2200, 100

array = fillarray(A, B, N)
print("Максимальное неудобство для бригады: ", end="")
print(maxdiff(array),"мм.")
