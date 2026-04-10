# Case 1: {key:key*key,......}

dict1={x:x*x for x in range(1,6)}
print(dict1)

# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# Case 2: {key:2^key,.....}

dict2={x:2**x for x in range(1,6)}
print(dict2)

# Output: {1: 2, 2: 4, 3: 8, 4: 16, 5: 32}