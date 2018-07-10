# 基于双向循环链表实现队列，使用双向链表的原因是，比起单向链表，
# 双向链表在双端操作的时间复杂度都是O(1)，而单向链表的尾部操作时间复杂度为O(n)


class QueueUnderflow(Exception):
    pass


class DoubleLinkedQueue(object):
    class Node:

        def __init__(self, item, prev=None, next=None):
            self.item = item
            self.prev = prev
            self.next = next

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def peek(self):
        """
        查询队首元素
        :return:
        """
        if self.is_empty():
            raise QueueUnderflow()
        return self.head.item

    def enqueue(self, item):
        """
        入队操作，采用追加的方式，保证head为队首(便于语义上的理解)
        :param item:
        :return:
        """
        node = DoubleLinkedQueue.Node(item)
        if self.is_empty():
            node.prev = node
            node.next = node
            self.head = node
        else:
            # 追加元素，在尾部添加
            rear = self.head.prev
            rear.next = node
            node.next = self.head
            self.head.prev = node

    def dequeue(self):
        if self.is_empty():
            raise QueueUnderflow()
        # 从首部出队，即：取出首部元素，将其短路(不再引用)
        head = self.head
        if head is head.next:
            # 如果只有一个元素：head = head.next = head.prev，需要特殊处理
            self.head = None
        else:
            self.head = head.next
            self.head.prev = head.prev
            head.prev.next = self.head

        return head.item


queue = DoubleLinkedQueue()

# True
print(queue.is_empty())

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# True
print(queue.peek() == 1)
# False
print(queue.is_empty())

# True
print(queue.dequeue() == 1)
# True
print(queue.dequeue() == 2)
# True
print(queue.dequeue() == 3)

# True
print(queue.is_empty())
