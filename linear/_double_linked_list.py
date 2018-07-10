# 双向链表


class DoubleLinkedList(object):
    class __Node:

        def __init__(self, item, prev=None, next=None):
            self.item = item
            self.prev = prev
            self.next = next

    def __init__(self):
        self._head = None
        self._rear = None

    def is_empty(self):
        return self._head is None

    def add(self, item):
        node = DoubleLinkedList.__Node(item, None)
        node.next = self._head
        # 双向链表增加prev指向新加入节点操作
        if self._head is not None:
            self._head.prev = node
        self._head = node

    def size(self):
        return len(self)

    def __len__(self):
        count = 0
        for _ in self:
            count += 1
        return count

    def remove(self, item):
        """ 删除操作遍历与单向链表并无区别，选择任意方向遍历即可，但删除时需要处理prev引用(指针) """
        curr = self._head
        prev = self._head.prev
        while curr.item != item:
            prev = curr
            curr = curr.next

        if prev is None:
            # 如果prev为空，说明删除的是头节点
            self._head = curr.next
            # 将新head节点的prev设置为None
            self._head.prev = None
        else:
            # 短路next指针(curr.next可以为空，表示删除的是最后一个节点)
            prev.next = curr.next
            # 短路prev指针(curr.next不能为空，否则没有prev指针)
            if curr.next is not None:
                curr.next.prev = curr.prev

    def clear(self):
        self._head = None

    def __iter__(self):
        """
        使LinkedList对象可以被迭代
        :return:
        """
        curr = self._head
        while curr is not None:
            item = curr.item
            curr = curr.next
            yield item


# 测试逻辑
lst = DoubleLinkedList()

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
