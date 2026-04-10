# Program: write a program to count number of occurrences of each vowel in the given strings

def count_vowel_frequency(input_string):
    """
    Count frequency of each vowel in the strings
    """

    vowel_frequency = {}
    vowels={'a','e','i','o','u'}

    # Iterate the input strings
    for char in input_string:
        if char in vowels:
            vowel_frequency[char] = vowel_frequency.get(char, 0) + 1

    return vowel_frequency




# User input
input_string=input("Enter a strings: ").lower()

# Get vowel frequency
v_frequency=count_vowel_frequency(input_string)

# Display output
for char,count in v_frequency.items():
    print(char,"->",count)