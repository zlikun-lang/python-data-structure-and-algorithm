# https://docs.python.org/3/library/collections.html#collections.namedtuple
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
point = Point(12, 36)
# <class '__main__.Point'> Point(x=12, y=36)
print(type(point), point)

Employee = namedtuple('Employee', 'name, age, department, salary')
ashe = Employee('Ashe', 18, 'Dev', 1800.00)
# <class '__main__.Employee'> Employee(name='Ashe', age=18, department='Dev', salary=1800.0)
print(type(ashe), ashe)

# ('name', 'age', 'department', 'salary')
print(ashe._fields)
# Employee(name='Ashe', age=21, department='Dev', salary=1800.0)
print(ashe._replace(age=21))
# Ashe
print(getattr(ashe, 'name'))
