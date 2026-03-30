# Python doesnt support Constructor overloading
# if we create multiple constructors in Python, PVM only consider the last one

class Test:

    def __init__(self):
        print("zero arg constructor")

    def __init__(self,x):
        print("one arg constructor")

    def __init__(self,x,y):
        print("two arg constructor")

#   t1=Test()  # TypeError
#   t2=Test(10)  #TypeError

t3=Test(10,20)  # valid

### We can do the same in python using *args

class Test2:

    def __init__(self,*args):
        print("Variable args constructor")

t1=Test2()  # Valid
t2=Test2()  # Valid

