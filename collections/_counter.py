# https://docs.python.org/3/library/collections.html#collections.Counter
# 统计字符出现个数？！

from collections import Counter

# Counter()
print(Counter())
# Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})
print(Counter('hello'))
# Counter({'name': 'Ashe', 'age': 18})
print(Counter({'name': 'Ashe', 'age': 18}))
# Counter({'dogs': 8, 'cats': 4})
print(Counter(cats=4, dogs=8))

c = Counter(cats=4, dogs=8)

# <itertools.chain object at 0x000001C5F2B8F7B8>
print(c.elements())
# [('dogs', 8), ('cats', 4)]
print(c.most_common(3))
c.subtract(Counter('hello'))
# Counter({'dogs': 8, 'cats': 4, 'h': -1, 'e': -1, 'o': -1, 'l': -2})
print(c)
