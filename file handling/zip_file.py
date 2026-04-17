from zipfile import *


def creating_zip():

    # create ZipFile class object
    z=ZipFile('zip1.zip','w',ZIP_DEFLATED)
    z.write('abc.txt')
    z.write('write.txt')
    z.close()
    print('zip file has been created successfully')

def reading_zip(filename):

    # Creating ZipFile class object
    z=ZipFile(filename,'r',ZIP_STORED)
    data=z.namelist()
    z.close()

    # Printing data in each file
    for file in data:
        f=open(file,'r')
        text_data=f.read()
        f.close()
        print(f'File name: {file}')
        print(text_data)



# Crating zip file :
creating_zip()

# Reading a names and content of files in zip file
reading_zip('zip1.zip')