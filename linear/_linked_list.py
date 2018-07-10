# LinkedList


class LinkedList(object):
    class __Node:

        def __init__(self, item, next=None):
            self.item = item
            self.next = next

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def add(self, item):
        node = LinkedList.__Node(item, None)
        node.next = self._head
        self._head = node

    def get_head(self):
        return self._head

    def size(self):
        curr = self._head
        count = 0
        while curr is not None:
            count += 1
            curr = curr.next
        return count

    def remove(self, item):
        curr = self._head
        prev = None
        while curr.item != item:
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
        while curr is not None:
            item = curr.item
            curr = curr.next
            yield item


# 测试逻辑
lst = LinkedList()

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
