"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
2) без сортировки
сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randint
from timeit import timeit


a = [randint(0, 1000) for i in range(11)]
b = [randint(0, 1000) for i in range(101)]
c = [randint(0, 1000) for i in range(1001)]
# d = [randint(0, 1000) for i in range(100)]


def mediana_func(lst):
    if len(lst) % 2 != 0:
        for i in range((len(lst) - 1) // 2):
            lst.remove(max(lst))
        return max(lst)
    else:
        for i in range(len(lst) // 2 - 1):
            lst.remove(max(lst))
        x = max(lst)
        lst.remove(max(lst))
        return (max(lst) + x) / 2


print('Время поиска медианы без сортировки в массиве из 11 элементов:')
print(timeit("mediana_func(a[:])", globals=globals(), number=100), end='\n\n')
# 0.00023829999999999685
print('Время поиска медианы без сортировки в массиве из 101 элемента:')
print(timeit("mediana_func(b[:])", globals=globals(), number=100), end='\n\n')
# 0.0073105000000000045
print('Время поиска медианы без сортировки в массиве из 1001 элемента:')
print(timeit("mediana_func(c[:])", globals=globals(), number=100), end='\n\n')
# 0.6219006
# print(mediana_func(d))
