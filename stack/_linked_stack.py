# 基本链表实现的栈结构，因为栈的特性：LIFO，所以可以使用单向链表实现，head节点即为栈顶


class StackUnderflow(Exception):
    pass


class LinkedStack(object):
    class Node:

        def __init__(self, item, next=None):
            self.item = item
            self.next = next

    def __init__(self):
        self._top = None

    def is_empty(self):
        """
        返回栈是否为空
        :return:
        """
        return self._top is None

    def top(self):
        """
        返回栈顶元素
        :return:
        """
        if self._top is None:
            raise StackUnderflow('in LinkedStack.top()')
        return self._top.item

    def push(self, item):
        """
        入栈
        :param item:
        :return:
        """
        self._top = LinkedStack.Node(item, self._top)

    def pop(self):
        """
        出栈
        :return:
        """
        if self.is_empty():
            raise StackUnderflow('in LinkedStack.pop()')
        node = self._top
        self._top = node.next
        return node.item


stack = LinkedStack()

# True
print(stack.is_empty())

stack.push(1)
stack.push(2)
stack.push(3)

# True
print(stack.top() == 3)

# False
print(stack.is_empty())

# True
print(stack.pop() == 3)
# True
print(stack.pop() == 2)
# True
print(stack.pop() == 1)

# True
print(stack.is_empty())

try:
    stack.pop()
except StackUnderflow as e:
    # in LinkedStack.pop()
    print(e)
