def mygenerator():
    yield 3
    yield 2
    yield 1

g = mygenerator()
'''for i in g:
    print(i)
'''  
'''  
value = next(g)
print(value)

value = next(g)
print(value)

value = next(g)
print(value)

print(sum(g))
'''
print(sorted(g))

# generator function

def countdown(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1
        
cd = countdown(4)

print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))

import sys

def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

print(sys.getsizeof(firstn(1000000)))

def first_generator(n):
    num = 0
    while num < n:
        yield num 
        num += 1
        
print(sys.getsizeof(first_generator(1000000)))

# fibonacci sequence

def fibonacci(limit):
    # 0 1 1 2 3 5 8
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b
        
fib = fibonacci(30)
for i in fib:
    print(i)
    
# generator expression

mygeneratorexp = ( i for i in range(1000000) if i % 2 == 0)
print(sys.getsizeof(mygenerator))

mylist = [ i for i in range(1000000) if i % 2 == 0]
print(sys.getsizeof(mylist))

