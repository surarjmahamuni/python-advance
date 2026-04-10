class Test:

    def m1(self):
        x=int(input("Enter first number: "))
        y=int(input("Enter second number: "))

        try:
            print("The division of two numbers is: ", x/y)



        except ArithmeticError:
            print("division by zero")

        except ValueError:
            print("Please enter a number")


       # We can write single except block and can handle multiple exceptions
        except (ZeroDivisionError, ValueError) as msg:
            print("Try again! because problem is: ",msg)


        # Default except block: we can use default except type to handle any type of exceptions.
        # we can use default except block to print exception information.

        except:
            print("Try running the program again")

        #Note : default except block should be always last except block. otherwise: SyntaxError




t=Test()
t.m1()


## Next all the representation of except-blocks are right

# except ZeroDivisionError:
# except (ZeroDivisionError):
# except ZeroDivisionError as msg:
# except (ZeroDivisionError) as msg:
# except (ZeroDivisionError, ValueError):
# except (ZeroDivisionError, ValueError) as msg:
# except: