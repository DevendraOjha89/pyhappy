class Employee:
	#anythin that is without self is termed as tatic method
	def calculatetax2():
		print("static method")
	def calculate_tax(self):
		print("calculate tax")
		
	def __init__(self):
		print("constructor called")
	def __del__(self):
		print("destructor called")
	
	def __str__(self):
		return "I love Python"

e = Employee()
Employee.calculatetax2()
print(e)
