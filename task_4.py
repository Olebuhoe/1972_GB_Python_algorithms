"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from random import randint
from timeit import timeit

""" Создание словарей (добавление данных) """


def dict_creat(n):
    dct = {}
    for i in range(n):
        dct.setdefault(i+1, randint(0, 1000))
    return dct


print('Время создания обычного словаря:')
print(timeit("dict_creat(1000)", globals=globals(), number=1000)/1000, end='\n')
print('Время создания упорядоченного словаря:')
print(timeit("OrderedDict(dict_creat(1000))", globals=globals(), number=1000)/1000, end='\n\n')

# Время создания упорядоченного словаря немного дольше обычного (на 15-18%)


""" Получение данных из словарей """


def get_elem(dct, n):
    for i in range(n):
        dct.get(i)
        # dct.setdefault(i)
    return dct


simple_dict = dict_creat(10000)
order_dict = OrderedDict(dict_creat(10000))
print('Время получения элемента обычного словаря:')
print(timeit("get_elem(simple_dict, 1000)", globals=globals(), number=1000)/1000, end='\n')
print('Время получения элемента упорядоченного словаря:')
print(timeit("get_elem(order_dict, 1000)", globals=globals(), number=1000)/1000, end='\n\n')

# Время работы сопоставимо, но опять хоть и незначительно, но больше в случае с упорядоченным словарем (и get немного
# быстрее, чем setdefault)


""" Удаление пар ключей и значений """


def pop_func(dct, n):
    for i in range(n):
        dct.popitem()
    return dct


simple_dict = dict_creat(10000)
order_dict = OrderedDict(dict_creat(10000))
print('Время работы функции pop_func для обычного словаря:')
print(timeit("pop_func(simple_dict, 100)", globals=globals(), number=100)/100, end='\n')
print('Время работы функции pop_func для упорядоченного словаря:')
print(timeit("pop_func(order_dict, 100)", globals=globals(), number=100)/100, end='\n\n')

# Время удаления пар ключей и значений упорядоченного словаря немного дольше обычного (на 15-18%)


""" Удаление элементов через DEL """


def del_func(dct, n):
    for i in range(n):
        del dct[i+1]
    return dct


simple_dict = dict_creat(100000)
order_dict = OrderedDict(dict_creat(100000))
print('Время работы функции del_func для обычного словаря:')
print(timeit("del_func(simple_dict, 1000)", globals=globals(), number=1), end='\n')
print('Время работы функции del_func для упорядоченного словаря:')
print(timeit("del_func(order_dict, 1000)", globals=globals(), number=1), end='\n\n')

# И снова операция с упорядоченным словарем длилась на ~15% дольше


""" Создание копии словаря """


def copy_dict(dct):
    return dct.copy()


simple_dict = dict_creat(10000)
order_dict = OrderedDict(dict_creat(10000))
print('Время создания копии обычного словаря:')
print(timeit("copy_dict(simple_dict)", globals=globals(), number=1000)/1000, end='\n')
print('Время создания копии упорядоченного словаря:')
print(timeit("copy_dict(order_dict)", globals=globals(), number=1000)/1000, end='\n\n')

# Создание копии упорядоченного словаря на порядок дольше.


# Можно сделать общий вывод, что выигрыша в скорости работы методов словарей в случае использования OrderedDict мы не
# получим, сравнивая с работой обычных словарей на последних версиях Python. Использовать OrderedDict есть смысл только
# сугубо в специфических случаях.
