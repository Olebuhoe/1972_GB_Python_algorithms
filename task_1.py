"""
Задание 1.
Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете,
опираясь на примеры с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""
# Тема идет действительно тяжело, но в целом по коду хоть долго и муторно, но разобрался. На данном этапе вносить
# изменения в виде переименования переменных не вижу смысла, как и заниматься откровенным копипастом. Возможностей для
# какого-то действительно реального улучшения кода исходя из имеющихся знаний и времени не вижу. Свое участие в данном
# задании предлагаю в виде двух маленьких функций для получения кодированной строки и декодирования имеющейся на
# основании ранее полученных дерева и словаря.

from collections import Counter, deque


def haffman_tree(s):
    count = Counter(s)
    sorted_elements = deque(sorted(count.items(), key=lambda item: item[1]))
    if len(sorted_elements) != 1:
        while len(sorted_elements) > 1:
            weight = sorted_elements[0][1] + sorted_elements[1][1]
            comb = {0: sorted_elements.popleft()[0],
                    1: sorted_elements.popleft()[0]}
            for i, _count in enumerate(sorted_elements):
                if weight > _count[1]:
                    continue
                else:
                    sorted_elements.insert(i, (comb, weight))
                    break
            else:
                sorted_elements.append((comb, weight))
    else:
        weight = sorted_elements[0][1]
        comb = {0: sorted_elements.popleft()[0], 1: None}
        sorted_elements.append((comb, weight))
    return sorted_elements[0][0]


code_table = dict()


def haffman_code(tree, path=''):
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')
    return code_table


# Функция для получения строки в закодированном виде:
def str_code(table, str):
    res = ''
    for i in str:
        res += table[i] + ' '
    return res


# Функция для раскодирования строки:
def str_decode(table, str):
    res = ''
    for i in str.split():
        for key, value in table.items():
            if i == value:
                res += key
    return res


if __name__ == '__main__':
    code_table_1 = dict(haffman_tree("beep boop beer!"))
    print(code_table_1)
    s = "beep boop beer!"
    print(haffman_code(haffman_tree(s)))
    a = str_code(code_table, s)
    print(a)
    b = str_decode(code_table, a)
    print(b)

