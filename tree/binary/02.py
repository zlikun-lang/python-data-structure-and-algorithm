class BinaryTree:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert_left(self, data):
        if self.left is None:
            self.left = BinaryTree(data)
        else:
            self.left = BinaryTree(data, left=self.left)

    def insert_right(self, data):
        if self.right is None:
            self.right = BinaryTree(data)
        else:
            self.right = BinaryTree(data, right=self.right)

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_root_value(self, new_value):
        self.data = new_value

    def get_root_value(self):
        return self.data

    def __repr__(self):
        return str(self.data)


bt = BinaryTree('*')
bt.insert_left('+')
bt.insert_right('-')

# * + -
print(bt.get_root_value(), bt.get_left_child(), bt.get_right_child())

bt.set_root_value('/')
# / + -
print(bt.get_root_value(), bt.get_left_child(), bt.get_right_child())

bt.insert_left(3)
bt.insert_right(4)

# 未能达成：(3 + 4) / (7 - 2)，原因是插入子节点时，只能在根节点上操作
# / 3 + None 4 None -
print(bt.get_root_value(),
      bt.get_left_child(),
      bt.get_left_child().get_left_child(),
      bt.get_left_child().get_right_child(),
      bt.get_right_child(),
      bt.get_right_child().get_left_child(),
      bt.get_right_child().get_right_child(),
      )
