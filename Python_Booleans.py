# Python Booleans
# https://www.w3schools.com/python/python_booleans.asp

print("print(5 > 3) : ", 5 > 3)
print("print(5 == 3) : ", 5 == 3)
print("print(5 < 3): ", 5 < 3)
print()
print("print(bool(5 < 3)) : ", bool(5 < 3))
print()
print("print(bool(\"Hello\") : ", bool("Hello"))
print("print(bool(5) : ", bool(5))
print("print(bool(\"abc\") : ", bool("abc"))
print("print(bool([\"orange\", \"cherry\"] : ", bool(["orange", "cherry"]))
print("print(bool(False), bool(None), bool(0), bool(""), bool(), bool(()), bool([]), bool({})) : ", bool(False), bool(None), bool(0), bool(""), bool(), bool(()), bool([]), bool({}))

# An object made from a class with a function that returns 0 or False

class myclass():
    def __len__(self):
        return 0
myobject = myclass()
print("myobject value: ", bool(myobject))

# Function return a boolean

def myFunction():
    return True
print ("myFunction:", myFunction())

# Function return a boolean using condition

y = bool(int(input("Please enter a boolean condition. 0 for False and 1 for True: ")))
def myFunction2():
    return y

if myFunction2():
    print("myFunction2 returns True")
else:
    print("myFunction2 returns False")

# Check if an object is an integer or not

x = input("Please enter an integer: ")
try:
    try:
        x = int(x)
        print("is", x, "integer?", isinstance(x, int))
    except:
        x = float(x)
        print("is", x, "float?", isinstance(x, float))
except:
    print("is", x , "string?", isinstance(x, str))