# 二叉堆实现优先队列(PriorityQueue)
# 这里使用列表实现二叉堆，其本质是一个有序的完全二叉树，索引从1始计，每个节点的左子节点索引为节点索引*2，右子节点为节点索引*2+1
# 反过来一个子节点其父节点的索引为子节点索引//2，根据该特性，可以快速上浮、下沉元素


class BinaryHeap(object):

    def __init__(self):
        """
        创建一个空的二叉堆对象
        """
        self.heap_list = [0]
        self.current_size = 0

    def insert(self, data):
        """
        插入一个数据项到二叉堆中
        :param data:
        :return:
        """
        # 完全二叉树中增加一个元素，即在队尾追加一个元素
        self.heap_list.append(data)
        # 最大索引计数器(因为0被留空，所以最大索引即为列表长度)
        self.current_size += 1
        # 上浮追加的元素，将其放在合适的位置上
        self._perc_up(self.current_size)

    def _perc_up(self, i):
        """
        将小的节点向上升，直到其父节点值比之小结束
        :param i:
        :return:
        """
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i //= 2

    def find_min(self):
        """
        返回堆中最小项，最小项仍保留堆中(仅作查看，不删除)
        :return:
        """
        # 堆顶元素即为最小元素，索引从1开始计
        return self.heap_list[1]

    def del_min(self):
        """
        返回堆中的最小项，同时从堆中删除
        :return:
        """
        # 堆顶元素即为最小项，移走该节点后，原来的堆变成两个子堆，为了恢复堆结构
        # 1、用最后一个节点来代替根节点，然后移走最后一个节点，此时堆成为了一个完整的完全二叉树，但其未必须仍然是一个堆(堆的有序性)
        # 2、为了保证新结构仍是一个堆，需要将新节点下沉(与上浮操作相反)，以达到将最小节点移动到堆顶的目的
        # 取出堆顶元素
        data = self.heap_list[1]
        # 将最后一个节点值赋值给堆顶节点
        self.heap_list[1] = self.heap_list[self.current_size]
        # 删除最后一个节点
        # del self.heap_list[self.current_size]
        self.heap_list.pop()
        # 计数减一
        self.current_size -= 1
        # 执行下沉逻辑
        self._perc_down(1)
        return data

    def _perc_down(self, i):
        while i * 2 <= self.current_size:
            # 查找小的子节点
            mc = self._min_child(i)
            # 比较当前节点值与其较小子节点值，如果比之大，则交换
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            # 循环交换，直到当前节点比之较小子节点小时停止
            i = mc

    def _min_child(self, i):
        """
        返回较小子节点(直接左右子节点)
        :param i:
        :return:
        """
        if i * 2 + 1 > self.current_size:
            # 没有右子节点，直接返回左子节点
            return i * 2
        else:
            # 否则有右子节点
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                # 如果左子节点比右子节点小，返回左子节点
                return i * 2
            else:
                # 否则返回右子节点
                return i * 2 + 1

    def is_empty(self):
        """
        返回堆是否为空
        :return:
        """
        return self.current_size == 0

    def size(self):
        """
        返回堆中数据项个数
        :return:
        """
        return self.current_size

    def build_heap(self, lst):
        """
        从一个列表构建一个新堆
        :param lst:
        :return:
        """
        if len(lst) == 0:
            return
        # 取列表中间一个元素，作为堆顶
        i = len(lst) // 2
        # 第0位将留空，所以最后一个节点的索引即为列表长度
        self.current_size = len(lst)
        # 构建堆列表，前面拼接一个元素，值为0(任意)
        self.heap_list = [0] + lst
        # 对堆顶执行下沉操作(保证顺序)
        while i > 0:
            self._perc_down(i)
            i -= 1


heap = BinaryHeap()
heap.insert(5)
heap.insert(7)
heap.insert(3)
heap.insert(11)
# 3
print(heap.find_min())
# 3
print(heap.del_min())
# 5
print(heap.del_min())
# 7
print(heap.del_min())
# 11
print(heap.del_min())
# True
print(heap.is_empty())

heap.build_heap([4, 1, 7, 3, 9, 5, 2, 6, 8])
# 1
print(heap.find_min())
# 1
print(heap.del_min())
# 2
print(heap.del_min())
# 3
print(heap.del_min())
# False
print(heap.is_empty())
# 6
print(heap.size())
