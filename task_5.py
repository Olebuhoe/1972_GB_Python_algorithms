"""
Задание 5. На закрепление навыков работы со стеком
Реализуйте собственный класс-структуру "стопка тарелок".
Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.
Структура должна предусматривать наличие нескольких стопок.
Создание новой стопки происходит при достижении предыдущим
стеком порогового значения.
После реализации структуры, проверьте ее работу на различных сценариях.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стопки можно реализовать добавлением нового пустого массива
в массив стопок (lst = [[], [], [], [],....]).
"""


class StackClass:
    def __init__(self):
        self.elems = [[]]

    def push_in(self, el):
        if len(self.elems[-1]) < 3:
            for i in range(len(self.elems)):
                if len(self.elems[i]) < 3:
                    self.elems[i].append(el)
                    break
        else:
            self.elems.append([])
            self.elems[-1].append(el)

    def pop_out(self):
        if len(self.elems[-1]) > 1:
            return self.elems[-1].pop()
        else:
            return self.elems.pop()

    def get_val(self):
        return self.elems[-1][-1]

    def stack_size(self):
        return f'Стопок - {len(self.elems)}, тарелок в них - {3*(len(self.elems)-1) + len(self.elems[-1])}'


if __name__ == '__main__':
    stack_1 = StackClass()
    i = 0
    while i < 9:
        stack_1.push_in(f'{i+1} plate')
        i += 1
    print(stack_1.elems)
    stack_1.push_in('10 plate')
    stack_1.push_in('11 plate')
    stack_1.push_in('12 plate')
    stack_1.push_in('13 plate')
    stack_1.push_in('14 plate')
    print(stack_1.elems)
    stack_1.pop_out()
    print(stack_1.elems)
    # stack_1.pop_out()
    # print(stack_1.elems)
    print(stack_1.get_val())
    print(stack_1.stack_size())
