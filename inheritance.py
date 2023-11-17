#Inheritance in Python
#Calling a Super Method

class A:
	def __init__(self, n='Rahul'):
		self.name = n

class B(A):
	def __init__(self, roll):
		self.roll = roll
		A.__init__(self,'Hero') # We can also make it using  -->           super().__init__("Hero")

object = B(23)
print(object.name) # Prints Hero


#Multiple inheritance
# Python program to demonstrate
# super()

class Class1:
	def m(self):
		print("In Class1")

class Class2(Class1):
	def m(self):
		print("In Class2")
		super().m()

class Class3(Class1):
	def m(self):
		print("In Class3")
		super().m()

class Class4(Class2, Class3):
	def m(self):
		print("In Class4") 
		super().m()
	
print(Class4.mro())		 #This will print list
print(Class4.__mro__)	 #This will print tuple


