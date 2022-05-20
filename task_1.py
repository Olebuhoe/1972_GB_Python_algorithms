"""
Задание 1.	Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""


def calculator():
    oper = input('Введите операцию (+, -, *, /) или 0 для выхода: ')
    if oper == '0':
        print('Спасибо за то, что пользовались нашим калькулятором')
    elif oper == '-' or oper == '+' or oper == '*' or oper == '/':
        try:
            num_1 = float(input('Введите первое число: '))
            num_2 = float(input('Введите второе число: '))
        except ValueError:
            print('Это не число')
            return calculator()
        try:
            if oper == '/' and num_2 == 0:
                raise ZeroDivisionError('Делить на 0 нежелательно')
        except ZeroDivisionError as err:
            print(f'ZeroDivisionError: {err}')
            return calculator()
        if oper == '+':
            result = num_1 + num_2
            print(result)
            return calculator()
        elif oper == '-':
            result = num_1 - num_2
            print(result)
            return calculator()
        elif oper == '*':
            result = num_1 * num_2
            print(result)
            return calculator()
        elif oper == '/':
            result = num_1 / num_2
            print(result)
            return calculator()
        else:
            return calculator()
    else:
        try:
            raise ValueError('Введите правильное действие')
        except ValueError as err:
            print(f'ValueError: {err}')
            return calculator()


calculator()
