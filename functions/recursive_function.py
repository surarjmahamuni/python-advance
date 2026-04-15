def factorial(num):

    if num==0:
        result=1

    else:
        result= num * factorial(num - 1)

    return result

print(factorial(4))