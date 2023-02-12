""" 4) Вывести таблицу умножения для чисел от 2 до 9."""


def powertab():
    string = "\t"
    for i in [2, 8]:
        for j in range(2, 11):
            for k in range(4):
                print(f"{i + k:2} x {j:2} = {j * (i + k):3}{string}", end="")
            print()
        print()


powertab()
