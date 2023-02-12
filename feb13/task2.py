"""задача №2: Напишите программу, которая заполняет массив из N элементов степенями числа 2,
начиная с 2^1 до 2^N, в обратном порядке.
    Входные данные:
Входная строка содержит размер массива N . Необходимо сделать проверку,
что 0 < N ≤ 30 .
    Выходные данные:
Программа должна вывести содержимое массива: N первых степеней числа 2 в обратном
порядке (последний элемент должен быть равен 2^1).
"""


# функция основная
def Powerow(num):
    array = [2 ** i for i in range(num, 0, -1)]
    return array
    # def Recursion(num):
    #     return str(2 ** num) + " " + str(Recursion(num - 1)) if num != 1 else str(2**num)


# функция получения и проверки числа
def Check(num):
    if num.isdigit():
        num = int(num)
        if 0 < num <= 30:
            return True
    return False


# принимаем данные от пользователя
while True:
    number = input("N = ")
    if not Check(number):
        print("Вы ввели не число или число вне задданного диапазона от 0 до 100.")
        continue
    break
# выводим результаты в консоль
array = Powerow(int(number))
print(*array)
# print(Recursion(int(number)))
