# https://docs.python.org/3/library/collections.html#collections.OrderedDict
# 有序字典类型，其有序性是按插入顺序而非Key的自然排序

from collections import OrderedDict

d = OrderedDict.fromkeys('hello')

# <class 'collections.OrderedDict'> OrderedDict([('h', None), ('e', None), ('l', None), ('o', None)])
print(type(d), d)

# 移动到最后？
d.move_to_end('e')
# OrderedDict([('h', None), ('l', None), ('o', None), ('e', None)])
print(d)

# h
# l
# o
# e
for i in d:
    print(i)
