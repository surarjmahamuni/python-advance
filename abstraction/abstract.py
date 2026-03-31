# Abstract class is child class of ABC and has at least one abstract method
# compulsory both condition have to be true

from abc import *

class Employee(ABC):            # extended ABC class

    @abstractmethod             # abstract method
    def display(self):
        pass


# If we are creating child class for abstract class, then
# every abstract method of parent class needs to be implemented in child class
# otherwise child class is also abstract we cant create an object for the child class

class Employee1(Employee):

    def display(self):
        print("Its a concrete class.")

e1=Employee1()
e1.display()

# Abstract class can contain abstract and non-abstract method.
# child has to only provide implementation for default methods otherwise it becomes abstract too