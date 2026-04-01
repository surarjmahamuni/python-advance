class Test:

    def m1(self):
        x=int(input("Enter first number: "))
        y=int(input("Enter second number: "))

        try:
            print("The division of two numbers is: ", x/y)

        # except ArithmeticError:
        #     print("division by zero")
        #
        # except ValueError:
        #     print("Please enter a number")

        # We can write single except block and can handle multiple exceptions
        except (ZeroDivisionError, ValueError) as msg:
            print("Try again! because problem is: ",msg)

t=Test()
t.m1()