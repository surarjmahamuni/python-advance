""" Write a program to check whether the file exist or not.
if available then print the content of the file"""

import os

def file_exist_read(filename):

    if os.path.isfile('filename'):

        print(f'{filename} exists')

        f=open('filename','r')
        data=f.read()
        print(data)

    else:
        print(f'{filename} does not exist')

file_exist_read('Harryotter.txt')