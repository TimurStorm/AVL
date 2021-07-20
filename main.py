"""
====================================================================================
Теория(посмотреть https://russianblogs.com/article/23801660249/):
Авл-дерево - двоичное дерево.
Дерево-поиска - слева всегда наименьший эелемент, справа всегда наибольший.
Высота поддерева - максимальное количесво взаимосвязанных элементов в данном дереве.
Баланс - левая_высоста-правая_высота выбранного узла.
====================================================================================
Малый правый поворот:
1.когда баланс корня = +2(точно есть ребенок)
2.когда баланс ребенка = +1
    1)меняем местами родителя и ребенка( передаём правую/левую ветку приобмене)
Большой правый поворот:
1.когда баланс ребенка = -1
"""

"""
За основу взят пакет - treelib (https://treelib.readthedocs.io/en/latest/). 
Велосипедный код - плохо (ничтожный, хоть и новый, деревянный велосипед никому не нужен),
поэтому взятие чужого кода - хорошая и полезная практика для любого программиста. На что способен это пакет:
    1.Создание деревьев
    2.Добавление нового элемента с помощью метода create_node("значение узла", "идентификатор", "родитель")
    3.Красивое отображение в консоли с помощью метода show
    4.Удаление узла с помощью remove_node("идентификатор")
"""

from treelib import Tree, Node


# нереализованный
class MyNode(Node):
    def __init__(self, tag, identifier, data=None, parent=None, left=None, right=None):
        self.left = left
        self.right = right
        self.data = tag
        args = [arg for arg in [tag, identifier, data] if arg != None]
        super(MyNode, self).__init__(*args)


# возвращает тестовое дерево
def test_tree() -> Tree:
    tree = Tree()
    data = [
        {"tag": 1, "identifier": 1, "parent": None},
        {"tag": 2, "identifier": 2, "parent": 1},
        {"tag": 3, "identifier": 3, "parent": 1},
        {"tag": 4, "identifier": 4, "parent": 3},
        {"tag": 5, "identifier": 5, "parent": 3},
        {"tag": 6, "identifier": 6, "parent": 2}
    ]
    for node in data:
        tree.create_node(tag=node["tag"], identifier=node["identifier"], parent=node["parent"])
    return tree


"""
ПОВОРОТ НА ПРАВА

def right_rotate(self, node):
    if not node or not node.left:
        raise AssertionError(
            " right rotate to illegal node " + str(node))

    parent_node = node.parent
    node_left = node.left
    node.left = node_left.right

    if node.left:
        node.left.parent = node
    node_left.right = node
    node.parent = node_left
    if parent_node:
        if node == parent_node.left:
            parent_node.left = node_left
        else:
            parent_node.right = node_left
        node_left.parent = parent_node
    else:
        self.root = node_left
        node_left.parent = None"""

tree = test_tree()
tree.show()
text = tree.subtree(3)
print(type(text))
