"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры
ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
from timeit import timeit
import random


# Функция для получения списка
def list_filling(n):
    lst = []
    for i in range(n):
        lst.append(random.randint(0, 100))
    return lst


a = list_filling(100)


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


print(timeit("func_1(a)", globals=globals(), number=1000)/1000)
print(timeit("func_2(a)", globals=globals(), number=1000)/1000)

# Для оптимизации кода в функции было использовано list comprehension, который предсказуемо работает быстрее
