# Sets :  unordered, mutable, no duplicates

# creating a set
myset = {1,2,3,1,2}
myset_1 = set("Hello")  #unordered
print(myset)
print(myset_1)

# adding and removing elements
myset.add(4)
myset.add(5)
myset.add(6)
print(myset)
myset.remove(1)
myset.discard(8)    # no error if element not found
myset.pop()
myset_1.clear()     # clears the whole set
print(myset)
print(myset_1)

# looping throught set
for i in myset:
    print(i, end = " ")
print("\n\n")

#serching elements in set
if 5 in myset:
    print("Yes")
else:
    print("No")

print("\n\n")

# union and intersection of set

odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

u = odds.union(evens)
print(u)
print("\n")

i = odds.intersection(primes)
print(i)

diff = odds.difference(primes)
print(diff)

symm_diff = odds.symmetric_difference(primes)
print(symm_diff)

odds.update(evens)
print(odds)

evens.intersection_update(primes)
print(evens) 

setA = {1,2,3,4,5,6}
setB = {1,2,3}

print(setB.issubset(setA))
print(setB.issuperset(setA))
print(setA.isdisjoint(setB))
