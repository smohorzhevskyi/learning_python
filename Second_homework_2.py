"""
Напишите lambda функцию для поиска в заданном списке строк таких значений, длина которых равна шести.
Вернуть список всех элементов, удовлетворяющих данному условию.
"""

user_input = input("Введите список строк ").split()
new_list = filter(lambda i: len(i) == 6, user_input)
print(list(new_list))