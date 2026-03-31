# Any class member which accessible from the same class or outside of the class is Public

class Test:
    def __init__(self):
        self.a=10
        self._b=20
        self.__c=30    # not a private/special purpose variable

    def m1(self):
        print("m1() is public method")

    def m2(self):
        print("m2() is public method")
        print("a: ",self.a)
        print("_b: ",self._b)

       # print("_c: ",self.__c)    # not a private/special purpose variable

t=Test()

print(t.a)
print(t._b)
#print(t.__c)  # not a private/special purpose variable

t.m1()
t.m2()