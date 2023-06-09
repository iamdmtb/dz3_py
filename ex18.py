# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
import numpy as np
import math
N = int(input("Введите количество цифр: "))
arr1 = np.array([int(input()) for i in range(N)])
x = int(input("Введите цифру, к которой нужно найти ближайшее число: "))
arr2 = np.array([math.fabs(i - x) for i in arr1]) #чтобы не писать цикл на определение положеитльного и отрицательного, взял просто модуль..
print(f"К указанной цифре {x} ближайшие числа в массиве = {arr1[np.where(arr2 == arr2.min())]}")