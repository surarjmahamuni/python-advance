############ + Operator ############

# both operators needs to be string type

s='Python'+'engineer' # valid
#s='Python'+10        # Invalid --> both needs to be string in python



########### * Operator  ###############

# one operator needs to be int and other one string type

s = 'Python Engineer' * 3 # Valid
s = 3 * 'Python Engineer' # also valid

#s='Python Engineer' * 2.0 --> Invalid
#s='Python' * 'Python'  --> Invalid



########### in, not in --> Membership Operators ###########

s1= "Python Programming"
s2= "Python"

print("Membership Operators")


if s2 in s1:
    print("s2 is present in s1")
else:
    print("s2 is not present in s1")



##############  (<,<=,>,>=,==,!=) Comparison Operator for String  ###########

s1="Python"
s2="Pycharm"
print()
print("Comparison Operators")

if s1>s2:
    print("{} is greater than {}".format(s1,s2))  # "t" from Python is greater than "c" in Pycharm
elif s1<s2:
    print("{} is less than {}".format(s1,s2))
else:
    print("{} is equal to {}".format(s1,s2))



