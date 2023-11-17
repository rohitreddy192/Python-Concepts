# Python program to show that the variables with a value 
# assigned in class declaration, are class variables

# Class for Computer Science Student
class CSStudent:
	stream = 'cse'				 # Class Variable
	def __init__(self,name,roll):
		self.name = name		 # Instance Variable
		self.roll = roll		 # Instance Variable

# Objects of CSStudent class
a = CSStudent('Geek', 1)
b = CSStudent('Nerd', 2)

print(a.stream) # prints "cse"
print(b.stream) # prints "cse"
print(a.name) # prints "Geek"
print(b.name) # prints "Nerd"
print(a.roll) # prints "1"
print(b.roll) # prints "2"

# Class variables can be accessed using class
# name also
print(CSStudent.stream) # prints "cse"

# Now if we change the stream for just a it won't be changed for b
a.stream = 'ece'
print(a.stream) # prints 'ece'
print(b.stream) # prints 'cse'

# To change the stream for all instances of the class we can change it 
# directly from the class
CSStudent.stream = 'mech'

print(a.stream) # prints 'ece'
print(b.stream) # prints 'mech'

"""
Note: All variables which are assigned a value in the class declaration are class variables. 
And variables that are assigned values inside methods are instance variables.
 
"""


#Class Methods vs Static Methods

class MyClass:
    class_var = 10

    @classmethod
    def class_method(cls):
        return cls.class_var * 2

    @staticmethod
    def static_method(value):
        return value * 2

# Using both methods to achieve similar functionality
print(MyClass.class_method())     # Output: 20 (using class method)
print(MyClass.static_method(5))   # Output: 10 (using static method)

