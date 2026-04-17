""" Write a program to check whether the file exist or not.
 if it exist then count number of lines, words and numbers"""

import os
def count_lwn(filename):

    # Check if the file exist or not
    if os.path.isfile(filename):

        # To read the number of lines and words and characters
        line_count=word_count=char_count=0

        f=open(filename,'r')
        for line in f:
            # count lines
            line_count=line_count+1

            # count words
            w_per_lcount=len(line.split())
            word_count = word_count + w_per_lcount

            # count characters
            ch_per_line=len(line)
            char_count=char_count+ch_per_line

        print(f"number of lines are {line_count} and words are {word_count} and chars are {char_count}")
    else:
        print("file not exist")


count_lwn('HarryPotter.txt')

