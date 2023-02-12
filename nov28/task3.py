"""
3) Вывести ромб из звездочек. С клавиатуры вводится нечетное число N - количество звездочек (это
максимальное количество звёздочек ромба в самой длинной строке и одновременно количество строк, из
которых состоит ромб). В случае если, пользователь введет четное число, необходимо вывести сообщение о
неправильных входных данных, и снова потребовать ввод, до тех пор, пока не будет введено нечетное число."""


def showtriangle(n):
    for i in range((-n // 2 + 1) * 2, (n // 2 + 1) * 2, 2):
        print(
            " " * ((n - (n * 2 - (n // 2) * 2 - abs(i) - 1)) // 2)
          + "*" * (n * 2 - (n // 2) * 2 - abs(i) - 1))
    # for i in range(1, n+1, 2):
    #     print(" " * ((n - i)//2) + "*" * i)
    # for j in range(n // 2, 1, -1):
    #     print(" " * ((n - j)//2) + "*" * j)


def check(num):
    if not num.isdigit():
        print("Вы ввели не число.")
        return False
    if not int(num) % 2:
        print("Вы ввели четное число.")
        return False
    return True


while True:
    N = input("N = ")
    if not check(N): continue
    showtriangle(int(N))
    break