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
Это файл для пятого скрипта
"""
from pympler import asizeof

# Задание с курса "Алгоритмы и структуры данных на Python", 5 урок, задание 2.


class HexNum:
    def __init__(self, num):
        self.hex_num = hex(num).upper()[2:]

    def __str__(self):
        return self.hex_num

    def __add__(self, other):
        if isinstance(other, HexNum):
            return (hex(int(self.hex_num, 16) + int(other.hex_num, 16))).upper()[2:]
        else:
            raise TypeError('Один из объектов не является объектом класс HexNum')

    def __mul__(self, other):
        if isinstance(other, HexNum):
            return (hex(int(self.hex_num, 16) * int(other.hex_num, 16))).upper()[2:]
        else:
            raise TypeError('Один из объектов не является объектом класс HexNum')


hex_num1 = HexNum(5468)
print(asizeof.asizeof(hex_num1))                                                  # Полученное значение 264


class HexNum:
    __slots__ = ['hex_num']

    def __init__(self, num):
        self.hex_num = hex(num).upper()[2:]

    def __str__(self):
        return self.hex_num

    def __add__(self, other):
        if isinstance(other, HexNum):
            return (hex(int(self.hex_num, 16) + int(other.hex_num, 16))).upper()[2:]
        else:
            raise TypeError('Один из объектов не является объектом класс HexNum')

    def __mul__(self, other):
        if isinstance(other, HexNum):
            return (hex(int(self.hex_num, 16) * int(other.hex_num, 16))).upper()[2:]
        else:
            raise TypeError('Один из объектов не является объектом класс HexNum')


hex_num2 = HexNum(5468)
print(asizeof.asizeof(hex_num2))                                                   # Полученное значение 96


class HexNum:
    __slots__ = ('hex_num')

    def __init__(self, num):
        self.hex_num = hex(num).upper()[2:]

    def __str__(self):
        return self.hex_num

    def __add__(self, other):
        if isinstance(other, HexNum):
            return (hex(int(self.hex_num, 16) + int(other.hex_num, 16))).upper()[2:]
        else:
            raise TypeError('Один из объектов не является объектом класс HexNum')

    def __mul__(self, other):
        if isinstance(other, HexNum):
            return (hex(int(self.hex_num, 16) * int(other.hex_num, 16))).upper()[2:]
        else:
            raise TypeError('Один из объектов не является объектом класс HexNum')


hex_num3 = HexNum(5468)
print(asizeof.asizeof(hex_num3))                                                   # Полученное значение 40

# При использовании слотов для хранения атрибутов объекта класса видна явная экономия памяти, особенно, если хранить
# не в списке, а кортеже
