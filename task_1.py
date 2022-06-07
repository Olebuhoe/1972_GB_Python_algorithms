"""
Задание 1.
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
Обязательно доработайте алгоритм (сделайте его умнее)!
Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.
Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""
from random import randint
from timeit import timeit

a = [randint(-100, 100) for i in range(1000)]
print(a)


def bubble_rev_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_rev_sort_2(lst_obj):
    n = 1
    while n < len(lst_obj):
        ctrl_lst = lst_obj[:]
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        if ctrl_lst == lst_obj:
            break
        else:
            n += 1
    return lst_obj


print(bubble_rev_sort(a[:]))
print('Время работы функции bubble_rev_sort:')
print(timeit("bubble_rev_sort(a[:])", globals=globals(), number=100), end='\n\n')
print(bubble_rev_sort_2(a[:]))
print('Время работы функции bubble_rev_sort_2:')
print(timeit("bubble_rev_sort_2(a[:])", globals=globals(), number=100), end='\n\n')

# Обе функции работают примерно одинаковое время, доработанная совершенно незначительно дольше за счет проверки
# на совершение сортировки во время пройденной итерации. Т.е. выигрыша по времени практически нет, это логично, т.к. на
# несортированных больших списках вероятность окончания сортировки раньше прохождения всех итераций (перебора) очень
# мала. Доработка возможно будет эффективна на частично сортированных массивах.
