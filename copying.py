'''
    - shallow copy: one level deep, only references of nested child objects
    - deep copy: full independent copy
'''

import copy
org = [1,2,3,4,5]
cpy = org
cpy[0] = -10
print(cpy)
print(org)


org = [1,2,3,4,5, [6,7,8,9,10]]
#cpy = copy.copy(org)
#cpy = org.copy()
#cpy = list(org)
#cpy = org[:]
cpy = copy.deepcopy(org)
cpy[0] = -10
print(cpy)
print(org)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
p1 = Person("Alex", 27)
p2 = p1



