# startswith() and endswith() functions are used to check whether the given string starts or ends with the given substring

#user input
str=input("Enter the string:")
sub_str=input("Enter the sub string:")

#outputs:
output = str.startswith(sub_str)
print("{} string starts with {}: {}".format(str,sub_str,output))

output = str.endswith(sub_str)
print("{} string ends with {}: {}".format(str,sub_str,output))

#case sensitive
