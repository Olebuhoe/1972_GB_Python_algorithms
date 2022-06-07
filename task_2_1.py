"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)
сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randint
from timeit import timeit

a = [randint(0, 1000) for i in range(11)]
b = [randint(0, 1000) for i in range(101)]
c = [randint(0, 1000) for i in range(1001)]
# d = [randint(0, 1000) for i in range(100)]


def gnome_sort_mediana(lst):
	i = 1
	while i < len(lst):
		if lst[i - 1] <= lst[i]:
			i += 1
		else:
			lst[i - 1], lst[i] = lst[i], lst[i - 1]
			if i > 1:
				i -= 1
	if len(lst) % 2 != 0:
		return lst[(len(lst) - 1) // 2]
	else:
		return (lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) / 2


print('Время поиска медианы гномьей сортировкой в массиве из 11 элементов:')
print(timeit("gnome_sort_mediana(a[:])", globals=globals(), number=100), end='\n\n')
# 0.0017462999999999992
print('Время поиска медианы гномьей сортировкой в массиве из 101 элемента:')
print(timeit("gnome_sort_mediana(b[:])", globals=globals(), number=100), end='\n\n')
# 0.08026219999999999
print('Время поиска медианы гномьей сортировкой в массиве из 1001 элемента:')
print(timeit("gnome_sort_mediana(c[:])", globals=globals(), number=100), end='\n\n')
# 9.645496799999998
# print(gnome_sort_mediana(d))
