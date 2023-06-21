# Dictionaries : key-value pairs, unordered, mutable

# creating a dictionary
mydict = {"Name":"Max", "Age":38, "City":"Boston", "State":"Chicago", "Country":"USA"}
print(mydict)

mydict2 = dict(Name="Mary", Age = 27, City = "Tempe", State = "California", Country = "Lebanon")
print(mydict2)

print(mydict["Name"])

# adding key value pairs
mydict["Email"] = "max@gmail.com"
print( mydict)

# del/pop/popitem method for removing an element
mydict.pop("Email")
print(mydict)

mydict["Zipcode"] = 800006
print(mydict)

del mydict["Zipcode"]
print(mydict)

mydict.popitem() # deletes the last element
print(mydict)

# checking if a key is in dictionary
if "Name" in mydict:
    print(mydict["Name"])

    # using try and except
try:
    print(mydict["Zipcode"])
except:
    print("ERROR")
print("\n\n")

# looping through keys and values in dictionaries
for key in mydict:
    print(key,end=" ")

print("\n\n")

for keys in mydict.keys():  # does the same thing as above
    print(keys, end = " ")
print("\n")
for values in mydict.values():
    print(values, end = " ")
print("\n")
for key, value in mydict.items():
    print(key, value)

# copying 
mydict_copy = dict(mydict)
mydict_copy1 = mydict_copy.copy()

#merging dictionaries
mydict2.update(mydict)
print("\n", mydict2)