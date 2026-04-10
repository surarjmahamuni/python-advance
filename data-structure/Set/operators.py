s1={1,2,3,4}
s2={10,40,20}
s3={3,2,1,4}


###### Mathematical  ######
# s3= s1+s1  --> TypeError: unsupported operand type(s) for +: 'set' and 'set'

# s4= s1*2  --> TypeError: unsupported operand type(s) for +: 'set' and 'set'


####### Equality  ##########

print(s1==s2)  # False

print(s1 != s2)  # True

print(s1==s3)  # True  --> order doesnt matter


####### Relationship  ########
print("Relationship operators are not well built in python and we barely use it")

print(s1>s2)  # False

print(s1>=s2)  # False

print("why",s1<s2)  # False

print(s1<=s2)  # False

print(s1<=s3)  # True


######## Membership #######
print()

print(1 in s1)  # True

print(10 in s2)  # True

print(10 not in s1)  # True
