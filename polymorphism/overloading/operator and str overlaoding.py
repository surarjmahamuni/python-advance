class Book:

    def __init__(self,pages):
        self.pages=pages

    # Magic method for Operator overloading
    def __add__(self,other):
        return Book(self.pages+other.pages)

    # str()
    def __str__(self):
        return "Total no of pages: {}".format(self.pages)


b1=Book(100)
b2=Book(200)
b3=Book(300)

# print(b1+b2+b3) -->  without str(), output will be address of Book object

print(b1+b2+b3) # --> 600