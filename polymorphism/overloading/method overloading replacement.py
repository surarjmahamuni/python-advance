# Python doesnt support method overloading

# if we write multiple methods with same name and different number of args,
# then PVM will only call the last method

class Test:

    def m1(self):
        print("no-args method")

    def m1(self,x):
        print("single argument method")

    def m1(self,x,y):
        print("two argument method")

t=Test()
# t.m1()  ## TypeError: because last m1() method is expecting 2 args and we passed none.

#### Unlike Java, in Python we dont need to create multiple methods with same name just to pass multiple arguments
#### instead of doing that we can use *args


class Test2:
    def m1(self,*args):
        print("multiple argument method")

        total=0

        for i in args:
            total+=i

        print("Sum of numbers is: ", total)

t1=Test2()
t1.m1() # Sum of numbers is:  0
t1.m1(10,20,30,40) # 100

