"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list
Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее
2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее
3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее
Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""
from collections import deque
from random import randint
from timeit import timeit


# Функция для получения списка
def list_filling(n):
    array = []
    for i in range(n):
        array.append(randint(0, 100))
    return array


lst = list_filling(100000)
deq = deque(lst)


""" Пункт 1 """


def append_func(array, n):
    for i in range(n):
        array.append(randint(0, 100))
    return array


print('Время работы функции append_func со списком:')
print(timeit("append_func(lst, 10000)", globals=globals(), number=100)/100, end='\n\n')
print('Время работы функции append_func с деком:')
print(timeit("append_func(deq, 10000)", globals=globals(), number=100)/100, end='\n\n')

# В целом результаты сопоставимые, но с деком append почти на всех запусках отработал немного быстрее (скорее всего
# погрешность)


def pop_func(array, n):
    for i in range(n):
        array.pop()
    return array


print('Время работы функции pop_func со списком:')
print(timeit("pop_func(lst, 10000)", globals=globals(), number=100)/100, end='\n\n')
print('Время работы функции pop_func с деком:')
print(timeit("pop_func(deq, 10000)", globals=globals(), number=100)/100, end='\n\n')

# В целом результаты опять сопоставимы, но с деком pop опять почти на всех запусках отработал немного быстрее (хотя
# разница еще меньше, чем в случае с append)


# def extend_func(array_1, array_2):
#     for i in range(n):
#         array.extend()
#     return array

def extend_func(array_1, array_2):
    array_1.extend(array_2)
    return array_1


arr = list_filling(10000)
print('Время работы функции extend_func со списком:')
print(timeit("extend_func(lst, arr)", globals=globals(), number=100)/100, end='\n\n')
print('Время работы функции extend_func с деком:')
print(timeit("extend_func(deq, arr)", globals=globals(), number=100)/100, end='\n\n')

# Extend с деком отработал уже в разы быстрее, чем со списком


""" Пункт 2 """


def appendleft_func(array, n):
    for i in range(n):
        array.appendleft(randint(0, 100))
    return array


def insert_func(array, n):
    for i in range(n):
        array.insert(0, randint(0, 100))
    return array


print('Время работы функции insert_func со списком:')
print(timeit("insert_func(lst, 100)", globals=globals(), number=100)/100, end='\n\n')
print('Время работы функции appendleft_func с деком:')
print(timeit("appendleft_func(deq, 100)", globals=globals(), number=100)/100, end='\n\n')

# Время работы appendleft c деком на 2-3 порядка быстрее работы insert(0, elem) со списком


def popleft_func(array, n):
    for i in range(n):
        array.popleft()
    return array


def pop_func_2(array, n):
    for i in range(n):
        array.pop(0)
    return array


print('Время работы функции pop_func_2 со списком:')
print(timeit("pop_func_2(lst, 100)", globals=globals(), number=100)/100, end='\n\n')
print('Время работы функции popleft_func с деком:')
print(timeit("popleft_func(deq, 100)", globals=globals(), number=100)/100, end='\n\n')

# Время работы popleft c деком уже на 5-6 порядков быстрее работы pop(0) со списком


def extendleft_func(array_1, array_2):
    array_1.extendleft(array_2)
    return array_1


def insert_func_2(array_1, array_2):
    for i in range(len(array_2)):
        array_1.insert(0, array_2[i])
    return array_1


arr_2 = list_filling(100)
print('Время работы функции insert_func_2 со списком:')
print(timeit("insert_func_2(lst, arr_2)", globals=globals(), number=100)/100, end='\n\n')
print('Время работы функции extendleft_func с деком:')
print(timeit("extendleft_func(deq, arr_2)", globals=globals(), number=100)/100, end='\n\n')

# И в данном случае работа extendleft с деком на 5-6 порядков быстрее аналогичной функции для работы со списком


""" Пункт 3 """


def get_elem(array, n):
    for i in range(n):
        array[i] = array[i]
    return array


print('Время работы функции get_elem со списком:')
print(timeit("get_elem(lst, 10000)", globals=globals(), number=100)/100, end='\n\n')
print('Время работы функции get_elem с деком:')
print(timeit("get_elem(deq, 10000)", globals=globals(), number=100)/100, end='\n\n')

# Получение элемента списка по индексу в несколько раз быстрее получения элемента дека.
