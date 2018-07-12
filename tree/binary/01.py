# 基于 list/tuple 实现二叉数据


def binary_tree(data):
    """
    定义一个二叉树
    :param data:
    :return:
    """
    return [data, [], []]


def insert_left(node, data):
    """
    插入左子节点，这里与书上用法不同之处，返回的是插入后的左子节点
    :param node:
    :param data:
    :return:
    """
    # 取出原左子节点
    left_ = node.pop(1)
    if left_:
        # 不为空则插入新左子节点，将原来的左子节点作为新插入节点的左子结点
        node.insert(1, [data, left_, []])
    else:
        #   为空则插入新左子节点(原来的左子节点是空，忽略掉)
        node.insert(1, [data, [], []])
    return node[1]


def insert_right(node, data):
    """
    插入右子节点，原理与插入左子节点一致，返回插入后的右子节点
    :param node:
    :param data:
    :return:
    """
    right_ = node.pop(2)
    if right_:
        node.insert(2, [data, [], right_])
    else:
        node.insert(2, [data, [], []])
    return node[2]


def get_node_value(node):
    return node[0]


def set_node_value(node, new_value):
    node[0] = new_value


def get_left_child(node):
    return node[1]


def get_right_child(node):
    return node[2]


if __name__ == '__main__':
    # root = binary_tree('*')
    # left = insert_left(root, '+')
    # insert_left(left, 4)
    # insert_right(left, 3)
    # right = insert_right(root, '-')
    # insert_left(right, 7)
    # insert_right(right, 2)

    # 二叉树：3 + 4
    root = binary_tree('+')
    insert_left(root, 3)
    insert_right(root, 4)

    # ['+', [3, [], []], [4, [], []]]
    print(root)
    # +
    print(get_node_value(root))
    # [3, [], []]
    print(get_left_child(root))
    # [4, [], []]
    print(get_right_child(root))

    # 二叉树：(3 + 4) * (7 - 2)
    root = binary_tree('*')

    # 插入第二层左子节点
    left = insert_left(root, '+')
    # 插入第三层子节点
    insert_left(left, 3)
    insert_right(left, 4)

    # 插入第二层右子节点
    right = insert_right(root, '-')
    # 插入第三层子节点
    insert_left(right, 7)
    insert_right(right, 2)

    # ['*', ['+', [3, [], []], [4, [], []]], ['-', [7, [], []], [2, [], []]]]
    # ['*',
    #   ['+',
    #       [3, [], []],
    #       [4, [], []]
    #   ],
    #   ['-',
    #       [7, [], []],
    #       [2, [], []]
    #   ]
    # ]
    print(root)
