# Задача 1: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n = input("Введите трёхзначное число: ")
 
x = int(n[0])
x1 = int(n[1])
x2 = int(n[2])
 
print("Сумма цифр числа:", x + x1 + x2)