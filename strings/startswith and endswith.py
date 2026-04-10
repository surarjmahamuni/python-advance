# startswith() and endswith() functions are used to check whether the given strings starts or ends with the given substring

#user input
str=input("Enter the strings:")
sub_str=input("Enter the sub strings:")

#outputs:
output = str.startswith(sub_str)
print("{} strings starts with {}: {}".format(str,sub_str,output))

output = str.endswith(sub_str)
print("{} strings ends with {}: {}".format(str,sub_str,output))

#case sensitive
