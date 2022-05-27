"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
from collections import Counter
from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    return f'Чаще всего встречается число {Counter(array).most_common()[0][0]}, ' \
           f'оно появилось в массиве {Counter(array).most_common()[0][1]} раз(а)'


# print(func_1())
# print(func_2())
# print(func_3())
print('Время работы функции func_1:')
print(timeit("func_1()", globals=globals(), number=1000)/1000, end='\n\n')
print('Время работы функции func_2:')
print(timeit("func_2()", globals=globals(), number=1000)/1000, end='\n\n')
print('Время работы функции func_3:')
print(timeit("func_3()", globals=globals(), number=1000)/1000, end='\n\n')

# C помощью класса Counter() модуля collections получилось сделать код более лаконичным и красивым, но добиться
# ускорения работы функции не получилось, скорее всего из-за того, что Counter() - это по своей сути словарь, в данном
# случае работающий на наполнение, а наполнение словаря относительно затратное по времени действие из-за хеширования
# ключей. Плюс используемый метод most_common, создающий из словаря список кортежей, также ресурсоемок по времени.
