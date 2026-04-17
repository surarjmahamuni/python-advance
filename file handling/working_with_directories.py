def directory_functions():
    """ This function implements to different Directory functions"""

    import os

    # Current working directory
    cwd=os.getcwd()
    print(f'Current working directory is: {cwd}',end='\n')

    # Create a directory in the current directory
    os.mkdir('dir1')
    print("directory is created.\n")

    # create directory inside directory from current directory
    os.mkdir('dir1/dir2')
    print('Successfully created sub-directory\n')

    # To create multiple directories:
    os.makedirs('dir2/dir3/dir4')
    print('Successfully created directory and sub-directories\n')

    # To rename the directory:
    os.rename('dir2/dir3/dir4','dir2/dir3/dir5')
    print('Renamed the directory \n')

    # To print the content of current directory:
    dir_list=os.listdir('C:\\Users\\srmah\\PycharmProjects\\python-advance\\file handling')
    print(f'Content in the current directory:{dir_list}\n')

    # To print out the content of current and its sub-directories
    all_dir=os.walk('C:\\Users\\srmah\\PycharmProjects\\python-advance\\file handling')
    print(f'Current working directory and its sub-directories: {all_dir}\n')

    # display the content of current and sub-directories
    for dirpath,dirnames,filenames in all_dir:
        print(f'Directory path: {dirpath}')
        print(f'sub-directories: {dirnames}')
        print(f'filenames: {filenames}')
        print()

    # To remove directory or sub-directory
    os.rmdir('dir1/dir2')
    print('Successfully removed sub-directories')
    os.rmdir('dir1')

    # To remove multiple directories in the path
    os.removedirs('dir2/dir3/dir5')
    print('Successfully removed all sub-directories')



# Testing different directory functions
directory_functions()