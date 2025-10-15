from pprint import pprint
from typing import Callable
"""Подключение библиотеки pprint для более коректного вывода результата"""
def gen_bin_tree(height=3, Root=13, 
                left_leaf:Callable[[float], float] = lambda x: x -1, 
                right_leaf:Callable[[float], float] = lambda y: y + 1):

    """
    Рекурсивно генерирует бинарное дерево заданной высоты.

    Каждый узел дерева представлен в виде словаря с ключами:
    - "value": значение текущего узла;
    - "left": левое поддерево (или None, если достигнут лист);
    - "right": правое поддерево (или None, если достигнут лист).

    При каждой рекурсии значение левого потомка увеличивается на 1,
    а правого уменьшается на 1 относительно значения родительского узла.

    Returns:
  
    dict
        Словарь, описывающий структуру бинарного дерева.
    """
    height = int(height)
    Root = int(Root)

    if int(height) == 0:
        return {"value": Root, "left": None, "right": None}
    """Проверка, что значение узла не равно 0, для корректной работы """
    
    left_child = left_leaf(Root)
    right_child = right_leaf(Root)
    """
    Расчёт правого и левого поддерева
    """

    return {
        "value": Root,
        "left": gen_bin_tree(height-1,left_child, left_leaf, right_leaf),
        "right": gen_bin_tree(height-1, right_child, left_leaf, right_leaf)
    }
res = gen_bin_tree()


pprint(res)

