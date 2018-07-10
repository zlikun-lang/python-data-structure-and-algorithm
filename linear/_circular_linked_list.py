# 单向循环链表


class CircularLinkedList(object):
    class __Node:

        def __init__(self, item, next=None):
            self.item = item
            self.next = next

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def add(self, item):
        node = CircularLinkedList.__Node(item, None)
        if self.is_empty():
            # 如果是添加第一个节点，不需要遍历尾节点(循环链接：将尾节点的next指向头节点)
            self._head = node
            node.next = self._head
        else:
            # 添加的节点的next指向原来的head节点
            node.next = self._head
            # 遍历链表，找到尾节点，将其next指向新的head节点
            curr = self._head
            while curr.next != self._head:
                curr = curr.next
            curr.next = node
            # 更新head节点为新节点
            self._head = node

    def size(self):
        return len(self)

    def __len__(self):
        count = 0
        for _ in self:
            count += 1
        return count

    def remove(self, item):
        curr = self._head
        prev = None
        # 增加截止条件，否则会死循环
        while curr.item != item and curr.next != self._head:
            prev = curr
            curr = curr.next

        if prev is None:
            self._head = curr.next
        else:
            prev.next = curr.next

    def clear(self):
        self._head = None

    def __iter__(self):
        """
        使LinkedList对象可以被迭代
        :return:
        """
        curr = self._head
        if curr is None:
            return
        # 会少循环一次，所以在循环外补偿一次
        while curr.next != self._head:
            item = curr.item
            curr = curr.next
            yield item
        yield curr.item


# 测试逻辑
lst = CircularLinkedList()

lst.add(1)
lst.add(2)

# 2
print(lst.size())

lst.add(3)

# False 3
print(lst.is_empty(), lst.size())

# -> 3
# -> 2
# -> 1
for i in lst:
    print('->', i)

lst.remove(2)

# 2
print(lst.size())

lst.clear()

# True 0
print(lst.is_empty(), lst.size())
