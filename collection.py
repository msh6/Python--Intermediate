# Collections: counter, namedtuple, orderedDict, defaultDict, deque
from collections import Counter
a = "aaaaaabbbbbcc"
my_counter = Counter(a)     # creates a dict
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(1))
print(my_counter.most_common(1)[0][0])
print(list(my_counter.elements()))
print("\n\n\n")

from collections import namedtuple
Point = namedtuple("Point", "x,y")
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)
print("\n\n\n")

from collections import defaultdict
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['a'])
print(d['c'])
print("\n\n\n")

from collections import deque
d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
print(d)

d.pop()
print(d)

d.popleft()
print(d)

d.extendleft([4,5,6])
print(d)

d.rotate(1)
print(d)

d.rotate(-1)
print(d)
