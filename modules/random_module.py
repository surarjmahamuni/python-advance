"""
Different random module functions
"""""

from random import *

# random():
print('Print a random number between 0 and 1: ')
for i in range(5):
    print(random())

print()

# uniform(begin,end): begin and end inclusive
print('Print a random number between 0 and 11: ')
for i in range(5):
    print(uniform(0,11))

print()

# randint(begin,end): begin and end inclusive
print('Print a random value between 0 and 6: ')
for i in range(5):
    print(randint(0,6))

print()

# randrange(begin,end,step):begin and end-1 inclusive
print('Print a random value between 0 and 6: ',randrange(0,6,1))

# choice():
nums=[0,1,2,3,4,5,6,7,8,9]

print('Printing 5 random numbers between 0 and 9: ')
for i in range(5):
    print(choice(nums))