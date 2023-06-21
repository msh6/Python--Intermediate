# Lists: ordered, mutable, allows duplicate elements

mylist = ["banana", "apple", "cherry", True, 1, 0.5]
print(mylist)

# mylist2 = list()  # initialization method

# indexing the list
item = mylist[5]   
print(item)

# looping through list
for i in mylist:
    print(i)

# length of list
print(len(mylist))

# appending to list
mylist.append("dinosaur")
mylist.insert(1, "blueberry")
print(mylist)

# removing & pop method 
del_item = mylist.pop()
print(del_item)
print(mylist)
mylist.remove("cherry")
print(mylist)

# copying list
mylist2 = list(mylist.copy())
print(mylist2)
mylist3 = mylist[:]     # fast and effective way
print("mylist3 : ", mylist3)

# clearing the complete list
mylist2.clear()
mylist3.clear()
print(mylist2)

# reverse method
mylist.reverse()
print(mylist)

# sort method
# mylist.sort() - for sort method all elements have to 
# be of same type
# print(mylist)

# creating a list of numbers
num_list = [1] * 10
print(num_list)

# slicing
print("\n\n")
print(mylist)
print(mylist[1:5])
print(mylist[:4])
print(mylist[::-1]) #reverse

# running for loop for to add squares of numbers from a list
nums = [1,2,3,4,5]
squares = [i * i for i in nums]
print(nums, "\n", squares)