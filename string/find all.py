# there is no find all function in python
# we are writing a custom program to find all the occurrence of substring in given string

# find() function only returns first occurrence of the substring in the given string

s2="ABCABCABC"

index=s2.find("ABC")
print(index)             # it only returns 0 index

####### find_all()  #############

str1=input("Enter a string: ")
sub_str1=input("Enter a sub string: ")

#find the index of substring
index=str1.find(sub_str1)

#if index=-1
if index==-1:
    print("Sub-String not found")

#if we dont want to use count() function to count number of occurrences
count=0

#while its not -1
while index != -1:
    count=count+1

    print("substrtring: {} is present at index {}:".format(sub_str1,index))

    #keep looking for sub-string in remaining part of the given string
    index=str1.find(sub_str1,index+len(sub_str1),len(str1))

#print number of occurrences
print("Number of times sub-string: {} present in string: {} is {}".format(sub_str1,str1,count))

