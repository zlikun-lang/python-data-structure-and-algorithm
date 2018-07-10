# https://docs.python.org/3/library/collections.html#collections.ChainMap
# 表示尚不理解实际意义~

from collections import ChainMap
import builtins

pylookup = ChainMap(locals(), globals(), vars(builtins))
print(pylookup)

new_map = ChainMap({'name': 'zlikun', 'age': 120}, {'name': 'zlikun', 'salary': 3500.00})
# ChainMap({'name': 'zlikun', 'age': 120}, {'name': 'zlikun', 'salary': 3500.0})
print(new_map)
# [{'name': 'zlikun', 'age': 120}, {'name': 'zlikun', 'salary': 3500.0}]
print(new_map.maps)
