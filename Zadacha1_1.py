# Задача №1:
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.

# Пример:
# 5 -> 1 0 1 1 0

def coin():
    count_coin = int(input('Введите количество монеток: '))
    list_coin = []
    count = 0
    while count < count_coin:
        answer = int(input('Если Решкой - введите "1", если Орлом - введите "0": '))
        list_coin.append(answer)
        count += 1
    print(list_coin)
    reshka = list_coin.count(1)
    orel = list_coin.count(0)
    print(f'Решка = {reshka}')
    print(f'Орёл = {orel}')
    min_change_coin = ''
    if reshka < orel:
        min_change_coin = reshka
    else:
        min_change_coin = orel
    print(f'Минимальное количество монет для переворота составит {min_change_coin}')
coin()