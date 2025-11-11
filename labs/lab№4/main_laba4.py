from typing import Callable
from pprint import pprint

def gen_bin_tree(height='3', Root='13', 
                 left_leaf: Callable[[float], float] = lambda x: x + 1, 
                 right_leaf: Callable[[float], float] = lambda y: y ** 2):
    """
    Генерирует бинарное дерево заданной высоты с функциями для вычисления 
    значений левого и правого потомков каждого узла.

    Параметры:
    ----------
    height : str или int, по умолчанию '3'
        Высота бинарного дерева. Корень находится на уровне 0.
    Root : str или int, по умолчанию '100000'
        Значение корневого узла дерева.
    left_leaf : Callable[[float], float], по умолчанию lambda x: x + 1
        Функция для вычисления значения левого потомка узла.
    right_leaf : Callable[[float], float], по умолчанию lambda y: y ** 2
        Функция для вычисления значения правого потомка узла.

    Возвращает:
    ----------
    dict
        Бинарное дерево в виде вложенных словарей, где ключи — это значения узлов,
        а значения — список дочерних узлов (каждый дочерний узел также представлен 
        словарем).

    
    """
    
    height = int(height)
    Root = int(Root)

    if height == 0:
        return {Root}
    
    per = 0
    for i in range(height):
        if (height > 0):
            per += 2 ** height
            height -= 1
  
    lst = [Root]
    x = int((per + 1) / 2)
    for i in range(0, x):
        lst.append(left_leaf(lst[i]))
        lst.append(right_leaf(lst[i]))
        per -= 1

    nodes = [{str(val): []} for val in lst]

    # Шаг 2: связываем детей с родителями
    for i in range(len(lst)-1, -1, -1):
        left_idx = 2*i + 1
        right_idx = 2*i + 2
        children = []
        if left_idx < len(lst):
            children.append(nodes[left_idx])
        if right_idx < len(lst):
            children.append(nodes[right_idx])
        nodes[i][str(lst[i])] = children

    # Шаг 3: корень
    tree = nodes[0]
                 
    return tree

res = gen_bin_tree()
pprint(res)
