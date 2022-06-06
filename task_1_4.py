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
Это файл для четвертого скрипта
"""
from memory_profiler import profile
from random import randint
import numpy as np

# Задание с курса "Алгоритмы и структуры данных на Python", 1 урок, задание 3. Здесь вместо списка будем использовать
# np.array и произведем замеры


def dict_filling(n):
    return {i+1: randint(0, 100) for i in range(n)}


a = dict_filling(30000)


@profile
def top_3_company_profit_2(company_profit):
    top_3_company_prof = []
    i = 0
    while i < 20000:
        top_3_company_prof.append(max(company_profit, key=company_profit.get))
        company_profit.pop(max(company_profit, key=company_profit.get))
        i += 1
    return top_3_company_prof


top_3_company_profit_2(a)

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    16     22.3 MiB     22.3 MiB           1   @profile
    17                                         def top_3_company_profit_2(company_profit):
    18     22.3 MiB      0.0 MiB           1       top_3_company_prof = []
    19     22.3 MiB      0.0 MiB           1       i = 0
    20     22.5 MiB      0.0 MiB       20001       while i < 20000:
    21     22.5 MiB      0.3 MiB       20000           top_3_company_prof.append(max(company_profit, key=company_profit.get))
    22     22.5 MiB      0.0 MiB       20000           company_profit.pop(max(company_profit, key=company_profit.get))
    23     22.5 MiB      0.0 MiB       20000           i += 1
    24     22.5 MiB      0.0 MiB           1       return top_3_company_prof

"""
b = dict_filling(30000)


@profile
def top_3_company_profit_3(company_profit):
    top_3_company_prof = np.array([])
    i = 0
    while i < 20000:
        np.append(top_3_company_prof, max(company_profit, key=company_profit.get))
        # del company_profit[max(company_profit, key=company_profit.get)]
        company_profit.pop(max(company_profit, key=company_profit.get))
        i += 1
    return top_3_company_prof


top_3_company_profit_3(b)

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    17     34.0 MiB     34.0 MiB           1   @profile
    18                                         def top_3_company_profit_3(company_profit):
    19     34.0 MiB      0.0 MiB           1       top_3_company_prof = np.array([])
    20     34.0 MiB      0.0 MiB           1       i = 0
    21     34.1 MiB      0.0 MiB       20001       while i < 20000:
    22     34.1 MiB      0.0 MiB       20000           np.append(top_3_company_prof, max(company_profit, key=company_profit.get))
    23                                                 # del company_profit[max(company_profit, key=company_profit.get)]
    24     34.1 MiB      0.0 MiB       20000           company_profit.pop(max(company_profit, key=company_profit.get))
    25     34.1 MiB      0.0 MiB       20000           i += 1
    26     34.1 MiB      0.0 MiB           1       return top_3_company_prof

"""

# В случае использования np.array вместо списка мы может наблюдать хоть и небольшую, но экономию память в 0.3 MiB.
