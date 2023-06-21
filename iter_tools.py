''' itertools: product, permutations, 
combinations, accumulate, groupby 
and infinite iterators '''

# product
from itertools import product
a = [1, 2]
b = [3]
prod = product(a, b, repeat = 2)
print(list(prod))
print("\n")

# permutations
from itertools import permutations
a = [1,2,3]
perm = permutations(a)
print(list(perm))
permu = permutations(a, 2)
print(list(permu))

# combinations
from itertools import combinations, combinations_with_replacement
a = [1,2,3,4]
comb = combinations(a, 2)
print("\n", list(comb))
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))
print("\n")

# accumulate
from itertools import accumulate
import operator
a = [1,2,3,4]
acc = accumulate(a)
print(a)
print(list(acc))
b = [1,2,3,4]
accm = accumulate(a , func= operator.mul)
print(b)
print(list(accm))
c = [1,2,5,3,4]
accu = accumulate(c, func= max)
print(c)
print(list(accu))
print("\n")

# groupby
from itertools import groupby
def smaller_than_3(x):
    return x < 3
a = [1,2,3,4]
group_obj = groupby(a, key = lambda x : x < 3)
for key, value in group_obj:
    print(key, list(value))
print("\n")

# count, cycle and repeat
from itertools import count, cycle, repeat
for i in count(10):
    print(i)
    if i == 15:
        break
a = [1,2,3]
'''for i in cycle(a):
    print(i)'''
for i in repeat(a,10):
    print(i)

