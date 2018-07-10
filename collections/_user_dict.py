# https://docs.python.org/3/library/collections.html#collections.UserDict

from collections import UserDict, UserList, UserString

user_dict = UserDict({'name': 'zlikun', 'age': 120})
# <class 'collections.UserDict'> {'name': 'zlikun', 'age': 120}
print(type(user_dict), user_dict)

user_list = UserList(range(4))
# <class 'collections.UserList'> [0, 1, 2, 3]
print(type(user_list), user_list)

user_string = UserString('hello')
# <class 'collections.UserString'> hello
print(type(user_string), user_string)
