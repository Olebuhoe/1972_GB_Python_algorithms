"""
Задание 1.
Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python
На каждый скрипт нужно два решения - исходное и оптимизированное.
Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler
Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler
Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.
ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.
Это файл для третьего скрипта
"""
from random import randint
from pympler import asizeof

# Задание с курса "Алгоритмы и структуры данных на Python", 4 урок, задание 1: Приведен код, который позволяет сохранить
# в массиве индексы четных элементов другого массива.
# По сути задания нам необязательно хранить полученные данные в массиве, можно создать генератор, выдающий требуемые
# индексы изначального массива и при необходимости выгрузить их в список.


def list_filling(n):
    return [randint(0, 100) for i in range(n)]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# Генератор:
def func_2(nums):
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            yield i


print(asizeof.asizeof(func_1(list_filling(1000))))
print(asizeof.asizeof(func_2(list_filling(1000))))
print(asizeof.asizeof(*func_2(list_filling(1000))))

# Замеры показывают, что даже выгруженные из генератора данные занимают на 20-25% меньше памяти, чем список, не говоря
# уже про спящий генератор
