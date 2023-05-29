import numpy as np
N = int(input("Введите количество цифр: "))
arr1 = np.array([int(input()) for i in range(N)])
x = int(input("Введите цифру, которую нужно найти: "))
count = 0
for j in arr1:
    if j == x:
        count += 1
print(f"В заданном массиве, цифра {x} встречается {count} раз")