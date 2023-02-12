"""
Задача №3: Напишите программу, которая заполняет массив из N элементов случайными целыми
числами в диапазоне [A, B] и определяет количество элементов этого массива, у которых
вторая цифра в десятичной записи (число десятков) – чётная."""

from random import randint


def fillarray(n, a, b):
    return [randint(a, b) for _ in range(n)]


def count10even(arr):
    cnt = 0
    for i in arr:
        if not (i // 10) % 2:
            cnt += 1
    return cnt


def check(num):
    if num.isdigit(): return True
    print("Вы ввели не число.")
    return False


while True:
    N = input("N = ")
    if not check(N): continue
    A = input("A = ")
    if not check(A): continue
    B = input("B = ")
    if not check(B): continue
    array = fillarray(int(N), int(A), int(B))
    count = count10even(array)
    print(*array)
    print(count)
    break
