# Errors and Exception

x = -5

'''raising an exception
if x < 0:
    raise Exception("x has to positive:")
'''

'''using assertion
assert(x >= 0), "x is not positive"
'''

# try and except 
try:
    a = 5/0
except:
    print("an error occured")

try:
    a = 5/0
except Exception as e:
    print(e)

try:
    a = 5/0
    b = a + 'lll'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("Everything is fine")
finally:
    print("cleaning up")

# defining our own exception

class ValueToHighError(Exception):
    pass

class ValueToSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueToHighError("value to high")
    if x < 5:
        raise ValueToSmallError("value to small", x)
try:
    test_value(1)
except ValueToHighError as v:
    print(v)
except ValueToSmallError as v:
    print(v)

