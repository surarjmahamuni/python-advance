# In Python, we can access private members of the class anywhere within the same class
# but we cant access them from outside of the class (not directly at least and we dont use indirect way)

class Test:

    def __init__(self):
        self.__a=1              # private variable

    def __m1(self):             # private method
        print("This is private method")

    def m2(self):               # public instance method
       print(self.__a)          # accessing private variable
       print("Calling private method from public method")  # accessing private method

t=Test()

t.m2()               # Valid --> just calling public method

# t.__a              # invalid --> cant access private member from outside of the class
# t.__m1()           # invalid


########## Name Mangling ##################

# we cant access private members directly from outside of the class directly
# but python will store each private member with name
# _ClassName__VariableName

# so we can access __a and __m1() by using name mangling

print(t._Test__a)
t._Test__m1()