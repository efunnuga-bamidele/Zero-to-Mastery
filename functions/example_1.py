
def say_hello():
    print("Hellooooooo!")

# say_hello()


# parameters and Arguments

def getAge(age= 0):
    print(f"Hello, you are {age} years old")
 
#positional arguments
# getAge(33)

#keyword arguments
# getAge(age=33)

# without argument
# getAge()

def sum(num1, num2):
    return num1 + num2

# print(sum(4, 5))
total = sum(10, 5)
print(sum(10, total))

# Doc strings

def test(a):
    '''
    Info: this function tests and prints parameter a.
    '''
    print(a)

test("Hello")
print(test.__doc__)