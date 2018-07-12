# 二叉搜索树

class BinarySearchTree(object):
    class TreeNode:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    def insert(self, data):
        if data is None:
            return
        node = BinarySearchTree.TreeNode(data)
        if self.root is None:
            self.root = node
        else:
            BinarySearchTree._insert_node(self.root, node)

    @staticmethod
    def _insert_node(parent, node):
        if node is None or node.data is None:
            return
        if node.data < parent.data:
            # 如果插入节点值比父节点值小，将插入节点插入父节点的左子树
            if parent.left is None:
                parent.left = node
            else:
                BinarySearchTree._insert_node(parent.left, node)
        else:
            # 如果插入节点值比父节点值大(或相等)，将插入节点插入父节点的右子树
            if parent.right is None:
                parent.right = node
            else:
                BinarySearchTree._insert_node(parent.right, node)


# 声明一个无序列表
lst = [4, 1, 7, 3, 9, 5, 2, 6, 8]
# 使用二叉搜索树进行排序(LDR,中序遍历)
tree = BinarySearchTree()

for i in lst:
    tree.insert(i)


# 中序遍历二叉树
def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.data, end=',')
        in_order(node.right)


# 1,2,3,4,5,6,7,8,9,
in_order(tree.root)
print()


# 前序遍历二叉树
def pre_order(node):
    if node is not None:
        print(node.data, end=',')
        pre_order(node.left)
        pre_order(node.right)


# 4,1,3,2,7,5,6,9,8,
pre_order(tree.root)
print()


# 后序遍历二叉树
def post_order(node):
    if node is not None:
        post_order(node.left)
        post_order(node.right)
        print(node.data, end=',')


# 2,3,1,6,5,8,9,7,4,
post_order(tree.root)
print()
