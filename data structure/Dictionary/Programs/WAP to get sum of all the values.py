# Program: write program to find the sum of all the value sin the given dictionary

# User input
students={'kumar':92,'sheila':93,'randy':84,'dennis':65}

# Logic
totalmarks=0

# Iterate over the dictionary
for item in students.items():
    totalmarks=totalmarks+item[1]

# Printing output
print("Sum of all students marks is: ",totalmarks)

#o/p: Sum of all students marks is:  334
