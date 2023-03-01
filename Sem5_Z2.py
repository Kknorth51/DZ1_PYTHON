# Задача 2
# Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.
# 2 2
# 4

def sum(a, b):
    if b == 0:
        return a
    else:
        return sum(a+1, b-1)

A = int(input("Введите первое число (A): "))
B = int(input("Введите второе число (B): "))

result = sum(A, B)
print(f"{A} + {B} = {result}")