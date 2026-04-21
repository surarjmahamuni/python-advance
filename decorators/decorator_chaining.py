def decor_num1(func):
    """Decorator for function num()"""
    def inner1():
        print("Executing decor_num1")
        num1= func()
        return num1*num1
    return inner1

def decor_num2(func):
    """Decorator for function decor_num2()"""
    def inner2():
        num2= func()
        print("Executing decor_num2")
        return 2*num2
    return inner2

@decor_num2
@decor_num1
def num():
    return 20

print(num())