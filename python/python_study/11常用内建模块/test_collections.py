from collections import namedtuple,deque

Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print(p.x)


q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)


