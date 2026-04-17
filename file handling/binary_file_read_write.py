import os

def binary_read_write(filename):

    # check if file exist
    if os.path.isfile(filename):

        # Read the binary file
        fr=open(filename,'rb')
        binary_data=fr.read()
        print(f'Type of data exist in the file: {type(binary_data)}')

        # Writing data to another file
        fw=open('Happy Face Copy.png','wb')
        fw.write(binary_data)

        fr.close()
        fw.close()
        print(f'File has been created')


binary_read_write('Happy Face.png   ')