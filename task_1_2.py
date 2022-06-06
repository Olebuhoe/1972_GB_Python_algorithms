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
Это файл для второго скрипта
"""
from memory_profiler import profile
from random import randint

# Задание с курса "Алгоритмы и структуры данных на Python", 3 урок, задание 1: скрипт наполнения списка.


@profile
def list_filling(n):
    lst = []
    for i in range(n):
        lst.append(randint(0, 100))
    return lst


list_filling(100000)

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     5     19.1 MiB     19.1 MiB           1   @profile
     6                                         def list_filling(n):
     7     19.1 MiB      0.0 MiB           1       lst = []
     8     20.6 MiB      0.0 MiB      100001       for i in range(n):
     9     20.6 MiB      1.5 MiB      100000           lst.append(randint(0, 100))
    10     20.6 MiB      0.0 MiB           1       return lst

"""


# Используем list comprehensions:
@profile
def list_filling_2(n):
    return [randint(0, 100) for i in range(n)]


b = list_filling_2(10000)

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     6     31.3 MiB     31.3 MiB           1   @profile
     7                                         def list_filling_2(n):
     8     31.4 MiB      0.2 MiB      100003       return [randint(0, 100) for i in range(n)]

"""


# Используем функцию map для наполнения списка:
@profile
def list_filling_2(n):
    return list(map(lambda x: randint(0, 100), range(n)))


list_filling_2(100000)

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     6     31.3 MiB     31.3 MiB           1   @profile
     7                                         def list_filling_2(n):
     8     31.4 MiB      0.2 MiB      200001       return list(map(lambda x: randint(0, 100), range(n)))

"""

# Замеры показывают значительное уменьшение инкремента при использовании list comprehensions и map-функции
