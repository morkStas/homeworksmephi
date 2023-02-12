"""
Задача 3.
Оксана прибавляет к числу его последнюю цифру. Назовём такое действие «операцией».
К полученному числу она прибавляет его последнюю цифру, затем прибавляет к результату
его последнюю цифру и т.д. Оксана начинает с числа 1 и после первой операции получает
2, после второй — 4, после третьей — 8, после четвёртой — 16, после пятой — 22 (потому
что 16+6=22)."""

n = 1
counter = 0
treedigits = 0
last = 0
grades = [2 ** i for i in range(5, 23)]
firstgrade = 1000000
while n < 10000000:
    last = n
    counter += 1
    if counter == 15:
        print("Value after 15 iterations:", n)
    if n == 2022:
        print("Operations count to 2022:", counter)
    if len(str(n)) == 3:
        treedigits += 1
    if (n in grades) and (n < firstgrade):
        firstgrade = n
    n += n % 10
print("Treedigit values count:", treedigits)
print("Most biggest value up to 7 digit:", last)
print("Smallest grade of 2 after 32:", firstgrade)
