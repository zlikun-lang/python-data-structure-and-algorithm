# https://docs.python.org/3/library/collections.html#collections.deque
from collections import deque

d = deque('hello')
# <class 'collections.deque'> deque(['h', 'e', 'l', 'l', 'o'])
print(type(d), d)

d.append('!')
# deque(['h', 'e', 'l', 'l', 'o', '!'])
print(d)

d.appendleft(':')
# deque([':', 'h', 'e', 'l', 'l', 'o', '!'])
print(d)

# 2
print(d.count('l'))

d.extend('python')
# deque([':', 'h', 'e', 'l', 'l', 'o', '!', 'p', 'y', 't', 'h', 'o', 'n'])
print(d)

d.extendleft([1, 2, 3])
# deque([3, 2, 1, ':', 'h', 'e', 'l', 'l', 'o', '!', 'p', 'y', 't', 'h', 'o', 'n'])
print(d)

d.remove(2)
# deque([3, 1, ':', 'h', 'e', 'l', 'l', 'o', '!', 'p', 'y', 't', 'h', 'o', 'n'])
print(d)

d.reverse()
# deque(['n', 'o', 'h', 't', 'y', 'p', '!', 'o', 'l', 'l', 'e', 'h', ':', 1, 3])
print(d)

d2 = d.copy()
d.clear()

# deque([])
print(d)
# deque(['n', 'o', 'h', 't', 'y', 'p', '!', 'o', 'l', 'l', 'e', 'h', ':', 1, 3])
print(d2)
