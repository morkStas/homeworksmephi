"""     Напишите программу, которая заполняет массив первыми N натуральными числами 
и выводит его.
    Входные данные
Входная строка содержит размер массива N. Необходимо сделать проверку, 
что 0 < N ≤ 100.
    Выходные данные
Программа должна вывести содержимое массива: N последовательных натуральных чисел 
от 1 до N. """


def fillarray(num):
    arr = [i for i in range(1, num + 1)]
    return arr


def check(num):
    if num.isdigit():
        num = int(num)
        if 0 < num <= 100:
            return True
    print("Вы ввели не число или число вне заданного диапазона от 0 до 100.")
    return False


while True:
    number = input("N = ")
    if not check(number):
        continue
    array = fillarray(int(number))
    print(*array)
    break
