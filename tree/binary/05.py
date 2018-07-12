# heapq是python官方提供的二叉堆数据结构模块
# https://docs.python.org/3/library/heapq.html


import heapq

heap = []
heapq.heappush(heap, 4)
heapq.heappush(heap, 7)
heapq.heappush(heap, 2)
heapq.heappush(heap, 5)
heapq.heappush(heap, 3)

# 2
print(heapq.heappop(heap))
# 3
print(heapq.heappop(heap))
# 4
print(heapq.heappop(heap))
# 5
print(heapq.heappop(heap))
# # 7
# print(heapq.heappop(heap))

# IndexError: index out of range
# print(heapq.heappop(heap))


# 将列表堆化
lst = [6, 4, 2, 8]
heapq.heapify(lst)
# [2, 4, 6, 8]
print(lst)

# 删除最小元素，添加新元素
heapq.heapreplace(lst, 5)
# [4, 5, 6, 8]
print(lst)

# 合并多个堆
# [4, 5, 6, 7, 8]
print(list(heapq.merge(heap, lst)))
# [7, 4, 5, 6, 8]
print(list(heapq.merge(heap, lst, reverse=True)))

# 查询堆中最大的三个元素
# [8, 6, 5]
print(heapq.nlargest(3, lst))
# 查询堆中最小的三个元素
# [4, 5, 6]
print(heapq.nsmallest(3, lst))
