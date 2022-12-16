'''x = input('Введите число ')


def summa(x):
    if float(x) < 0:
        x = float(x) * (-1)
    number = 0
    for i in str(x):
        if i != '.':
            number += int(i)
    return number


print(f'Сумма чисел равна {summa(x)}')'''




'''n = int(input('Введите число: '))

def get_squerence(n):
    return [round((1 + 1 / x)**x, 5) for x in range (1, n + 1)]

nums = get_squerence(n)
print(nums)
print(round(sum(nums), 5))'''

import random
list = [0,1,2,3,4,5,6,7,8,9]
print ("Начальный список: " + str(list))
for i in range(len(list)-1, 0, -1):
    j = random.randint(0, i + 1)
    list[i], list[j] = list[j], list[i]
print ("Перемешанный список: " +  str(list))