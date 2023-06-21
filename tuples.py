# Tuples: ordered, immutable, allows duplicate elements

# creating a tuple
mytuple = ("Max", 38, "Boston", "Chicago", "USA")
print(type(mytuple))
print(mytuple)

# indexing 
for i in mytuple:
    print(i)

# checking for element
if "Boston" in mytuple: 
    print(bool(1))
else:
    print(bool(0))

print(mytuple.count(38)) #for checking duplicates

# slicing 
print(mytuple[1:3])
print(mytuple[::2]) #step 
print(mytuple[::-1]) #reversing

# unpacking
name, age, city, state, country = mytuple
print(name, age, city, state, country)

a, *b, c = mytuple
print(a)
print(b)
print(c)

#comparing the byte size of list and tuple
import sys

mylist = list(mytuple)
print("Size of mylist : ",sys.getsizeof(mylist), " bytes")
print("Size of mytuple : ", sys.getsizeof(mytuple), " bytes")

# measuring time of tuple and list creation for a million times
import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number = 1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number = 1000000))

# Working with tuples is more efficient than working with lists.