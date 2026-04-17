import os,datetime


def print_stats():

    stats=os.stat('stats.py')
    print(f'Printing stats of the file: {stats}')
    print(f'File size: {stats.st_size}')
    print(f'File type: {stats.st_mode}')
    print(f'Last modified: {stats.st_mtime}')



print_stats()