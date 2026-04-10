# there are so many methods in strings we can use to find what types of character the given strings contains

#isalpha()
print("AbCdeF".isalpha())

# isalnum()
print("A1b3e".isalnum())

#isdigit()
print("1234".isdigit())

#islower()
print("baa".islower())
print("123abc".islower())  # True

#isupper()
print("ABC".isupper())

#istitle()
print("The Title".istitle())

#isspace()
print("    ".isspace())

#outputs:
# True
# True
# True
# True
# True
# True
# True

###

#write a program to check type of character entered by the user

#user input
ch=input("Enter the character: ")

#check if ch is alph-numeric
if ch.isalnum():

    #if alpha
    if ch.isalpha():

        #if uppercase
        if ch.isupper():
            print("Uppercase")

        #if lowercase
        else:
            print("Lowercase")

    #if digit
    else:
        print("digit")

#is space
elif ch.isspace():
    print("space character")

#special character
else:
    print("special character")