"""
    - The difference between arguments and parameters
    - Positional and Keyword arguments
    - Default arguments
    - Variable-length arguments (*args and **kwargs)
    - Container unpacking into function arguments
    - Local vs Global arguments
    - Parameters passing (by value or by reference?)
    """
    
def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo(1, 2, 3, 4, 5, six=6, seven=7)
print("\n")
foo(1, 2, 3, 4, 5)
print("\n")
foo(1, 2, six=6, seven=7)
print("\n")

def foo(a, b, c):
    print(a, b, c)
    
my_list = [0,1,2]
foo(*my_list)
print("\n")

my_tuple = (0,1,2)
foo(*my_tuple)
print("\n")

my_dict = {'a':0, 'b':1, 'c':2}
foo(*my_dict)
print("\n")
foo(**my_dict)
print("\n")

# local vs global variable

def foo():
    global number
    x = number
    number = 3
    print('number inside function:', x)
    
number = 0
foo()

# unpacking
numbers = [1,2,3,4,5,6]     # works with tuple aswell
*beginning, last = numbers
print(beginning)
print(last)

beginning, *last = numbers
print(beginning)
print(last)

beginning, *middle, last = numbers
print(beginning)
print(middle)
print(last)

mylist = [1,2,3]
mytuple = (4,5,6)
myset = {7,8,9}

newlist = [*mylist, *mytuple, *myset]
print(newlist)

mydict1 = {'a':1, 'b':2}
mydict2 = {'c':3, 'd':4}
new_dict = {**mydict1, **mydict2}
print(new_dict)