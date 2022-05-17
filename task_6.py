"""
Задание 6. На закрепление навыков работы с очередью
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Реализуйте класс-структуру "доска задач".
Структура должна предусматривать наличие нескольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку
После реализации структуры, проверьте ее работу на различных сценариях
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


class TaskBoard:
    def __init__(self):
        self.base = []
        self.revision = []
        self.resolved = []

    def task_appearance(self, task):
        self.base.insert(0, task)

    def task_refinement(self):
        self.revision.insert(0, self.base.pop())

    def task_solv_aft_revision(self):
        self.resolved.insert(0, self.revision.pop())

    def task_solved(self):
        self.resolved.insert(0, self.base.pop())

    def burning_task(self):
        return self.base[-1]

    def base_size(self):
        return len(self.base)

    def revision_size(self):
        return len(self.revision)

    def resolved_size(self):
        return len(self.resolved)


if __name__ == '__main__':
    task_board = TaskBoard()
    print(task_board.base)
    print(task_board.revision)
    print(task_board.resolved)
    task_board.task_appearance('tsk_1')
    task_board.task_appearance('tsk_2')
    task_board.task_appearance('tsk_3')
    task_board.task_appearance('tsk_4')
    print(task_board.base)
    task_board.task_refinement()
    print(task_board.base)
    print(task_board.revision)
    task_board.task_solv_aft_revision()
    task_board.task_solved()
    print(task_board.base)
    print(task_board.revision)
    print(task_board.resolved)
    print(task_board.burning_task())
    print(task_board.base_size())
    print(task_board.revision_size())
    print(task_board.resolved_size())
