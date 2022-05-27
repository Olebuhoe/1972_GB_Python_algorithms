"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через timeit
Обязательно предложите еще свой вариант решения!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""
from timeit import timeit
from random import randint


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


# Предлагаю 4-м вариантом решение с циклом for:
def revers_4(enter_num, revers_num=''):
    for i in reversed(range(len(str(enter_num)))):
        revers_num += str(enter_num)[i]
    return revers_num


# То же, но без реверса:
def revers_4_1(enter_num, revers_num=''):
    for i in range(len(str(enter_num))):
        revers_num += str(enter_num)[(len(str(enter_num)) - 1) - i]
    return revers_num


# И для интереса мемоизируем рекурсию:
def memoize(f):
    cache = {}

    def decorate(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate


@memoize
def revers_5(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


n = randint(10000000, 100000000)
# print(n)
# print(revers_1(n))
# print(revers_2(n))
# print(revers_3(n))
# print(revers_4(n))
# print(revers_6(n))
print('Время работы функции revers_1:')
print(timeit("revers_1(n)", globals=globals(), number=1), end='\n\n')
print('Время работы функции revers_2:')
print(timeit("revers_2(n)", globals=globals(), number=1), end='\n\n')
print('Время работы функции revers_3:')
print(timeit("revers_3(n)", globals=globals(), number=1), end='\n\n')
print('Время работы функции revers_4:')
print(timeit("revers_4(n)", globals=globals(), number=1), end='\n\n')
print('Время работы функции revers_4_1:')
print(timeit("revers_4_1(n)", globals=globals(), number=1), end='\n\n')
print('Время работы функции revers_5:')
print(timeit("revers_5(n)", globals=globals(), number=1), end='\n\n')

# Самой долгой по времени выполнения ожидаемо стала функция с рекурсией. Затем идет вариант с циклом for, причем
# варианты с reversed и без него вполне сопоставимы. Далее - рекурсия с мемоизацией и быстрее него вариант с циклом
# while. Вполне возможно, что при более длинном входящем ряду for победил бы while, но сама суть задания не
# подразумевает очень длинных (по машинным меркам) последовательностей символов (чисел).
# И наш топ - функция со строковыми срезами, это лучший вариант, т.к. это встроенная строковая функция и логично, что
# она максимально оптимизирована.
