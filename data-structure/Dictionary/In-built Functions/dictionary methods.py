############## len() ###################

dict1={100:'A',200:'B',300:'C'}

print(len(dict1))  # 3


############## get(key), get(key,default) #################

print(dict1.get(100))  # returns A

print(dict1.get(700)) # returns None

print(dict1.get(200,'guest')) # B

print(dict1.get(800,'guest')) # guest --> returns default value


#Note: always better to use get() instead of using dict[key].
#      if ky not found, dict[key] returns KeyError


############# update() ##############

dict2={300:'D',400:'E',100:'F'}

dict1.update(dict2)

print(dict1)  # {100: 'F', 200: 'B', 300: 'D', 400: 'E'} --> 100 key value updated

dict1.update({800:'E'})
print(dict1)  #{100: 'F', 200: 'B', 300: 'D', 400: 'E', 800: 'E'}

#Note: we are updating dict1 on dict2.

