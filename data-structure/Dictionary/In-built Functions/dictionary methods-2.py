########## keys()  #########

dict1={100:'A',200:'B',300:'C',400:'D'}

keys=dict1.keys()
print(keys)  # dict_keys([100, 200, 300, 400])

#how to just get keys:

for key in dict1.keys():
    print(key)

# o/p:
# 100
# 200
# 300
# 400


###############  values()  ###########

values=dict1.values()
print(values)  # dict_values(['A', 'B', 'C', 'D'])

#how to get just values

for value in dict1.values():
    print(value)

# o/p:
# A
# B
# C
# D


############  items() ###########

items=dict1.items()
print(items)  # dict_items([(100, 'A'), (200, 'B'), (300, 'C'), (400, 'D')])

#how to get it item by item

for key,value in dict1.items():
    print(key,value)

# o/p:
# 100 A
# 200 B
# 300 C
# 400 D

