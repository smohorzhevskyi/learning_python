"""
Вывести на печать список чисел, которые делятся на 3 и кратны 8,в диапазоне от 1000 до 1500 (оба включены).
"""

for i in range(1000, 1501):
    if i % 3 == 0 and i % 8 == 0:
        print(i)
