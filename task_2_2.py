"""
Задание 2.
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections
defaultdict(list)
int(, 16)
reduce
2) через ООП
вспомните про перегрузку методов
__mul__
__add__
"""


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


if __name__ == '__main__':
    hex_num1 = HexNum(5468)
    print(hex_num1)
    hex_num2 = HexNum(9853)
    print(hex_num2)
    print(hex_num2 + hex_num1)
    print(hex_num2 * hex_num1)
