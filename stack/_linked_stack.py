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


# 栈的应用，判断一组数字是否是回文数[12321, 12344321]
def is_palindromic_number(num):
    # 将数字转换为字符串(序列)
    s = str(num)
    length = len(s)

    stack2 = LinkedStack()

    # 由回文数的特征可知，其一半的反序等于另一半
    for i in range(length // 2):
        stack2.push(s[i])

    # 依次出栈，取出入栈的数字，与右边部分比较
    flag = True
    # length - length // 2 是为了避免奇数位数字情形
    for j in range(length - length // 2, length):
        if stack2.pop() != s[j]:
            flag = False
            break

    return flag


# True
print(is_palindromic_number(12345654321))
# True
print(is_palindromic_number(1234554321))


# 栈的应用，通过栈模拟递归函数调用过程，实现阶乘计算
def not_recursion_factorial(num):
    stack2 = LinkedStack()
    # 入栈过程，[num, num - 1, num - 2, ..., 1]
    while num > 0:
        stack2.push(num)
        num -= 1

    # 出栈过程，执行计算：1 * ... * (num - 2) * (num - 1) * num
    result = 1
    while not stack2.is_empty():
        result *= stack2.pop()

    return result


print(not_recursion_factorial(4) == 24)
print(not_recursion_factorial(5) == 120)
print(not_recursion_factorial(6) == 720)
