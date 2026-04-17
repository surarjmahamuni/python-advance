def tell_and_seek():
    """Test the tell and seek function"""

    with open('abc.txt','r+') as f:
        print(f.tell())
        f.seek(4)
        f.write('Jacob\n')
        f.write('Timothy\n')
        print(f.tell())



tell_and_seek()