# random module

import random

a = random.random() # from range 0 to 1
print(a)

a = random.uniform(1, 10)
print(a)

a = random.randint(1, 10) # includes upper bound
print(a)

a = random.randrange(1, 10) # excludes upper bound
print(a)

a = random.normalvariate(0, 1)
print(a)

# random function for sequences

mylist = list("ABCDEFGHI")
a = random.choice(mylist)
print(a)

a = random.choice(mylist) # can have duplicates
print(a)

a = random.sample(mylist, 5) # no duplicates
print(a)

print(mylist)
random.shuffle(mylist) # shuffle method
print(mylist)

random.seed(1)
print(random.random())
print(random.randint(1, 10))

random.seed(2)
print(random.random())
print(random.randint(1, 10))

random.seed(1)
print(random.random())
print(random.randint(1, 10))

random.seed(2)
print(random.random())
print(random.randint(1, 10))

import secrets

a = secrets.randbelow(10)
print(a)

a = secrets.randbits(4)
print(a)

a = secrets.choice(mylist)
print(a)

import numpy as np

a = np.random.rand(3)
print(np.__version__)



