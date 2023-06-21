# converting a python dictionary in to json format

import json
from typing import Any

person = {"name":"John", "age":38, "city":"New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# converting dict to json str
personJSON = json.dumps(person, indent = 4)
# personJSON = json.dumps(person, indent = 4, sort_keys=True)
print(personJSON)

# converting dict to json file
with open("person.json", 'w') as file:
    json.dump(person, file, indent = 4)
# converting json str to dict
person_dict = json.loads(personJSON)
print("\n", person_dict)  

# reading from a json file
with open("person.json", 'r') as file:
    person_file = json.load(file)
    print("\n", person_file)

# writing a custom object to json
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("Max", 27)

# creating an encoder
def encode_user(o):
    if isinstance(o, User):
        return {"name": o.name, "age": o.age, o.__class__.__name__:True}
    else:
        return TypeError("Object of type user is not JSON serializable")
    
userJSON = json.dumps(user, default=encode_user)
print(userJSON)

# using the json default encoder

from json import JSONEncoder
class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, User):
            return {"name": o.name, "age": o.age, o.__class__.__name__:True}
        return JSONEncoder.default(self, o)
    
userJSONN =UserEncoder().encode(user)
print(userJSONN)

#converting json to python

def decoder_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct

user = json.loads(userJSON, object_hook=decoder_user)
print(type(user))
print(user.name)

