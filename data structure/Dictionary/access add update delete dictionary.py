
################ Accessing Dictionary ##################

dict1={1: "A", 2: "B", 3: "C"}

print(dict1[1]) # A
print(dict1[2]) # B
#print(dict[5])  --> KeyError

#########always do this, so we dont get KeyError
key=int(input("Enter a number: "))

if key in dict1:
    print("For {} is in dict and its value is: {} ".format(key, dict1[key]))
else:
    print("Key is not in dict")



###############  add, update Dictionary ###################
print()
dict2= {101: 'Shiva', 102: 'ketty', 103: 'Sheila'}

dict2[600]='mia' # key=600 is not there, so 600:'mia' will be added in dict
print(dict2)
#{101: 'Shiva', 102: 'ketty', 103: 'Sheila', 600: 'mia'}


dict2[101]='rodgers'
print(dict2)
#{101: 'rodgers', '101': 'ketty', 103: 'Sheila', 600: 'mia'}



############ deleting from Dictionary #########
print()

dict3= {101: 'Shiva', 102: 'ketty', 103: 'Sheila'}

del dict3[101]
print(dict3)  #{102: 'ketty', 103: 'Sheila'}

del dict3[102], dict3[103]
print(dict3)  # {}

#del dict3[101]  --> KeyError





