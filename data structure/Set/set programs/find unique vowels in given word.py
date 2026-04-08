#write a program to find unique vowels present in the given word

#user input
word=input("Please enter a word: ")

#core logic
vowels={"a","e","i","o","u"}  # make sure its set

#find unique characters in the word
s1=set(word)
print(s1)  # {'e', 'p', 'l', 'a'}

#find intersection between vowels and s1
s2= s1 & vowels

#print output
print(s2)  # {'e', 'a'}