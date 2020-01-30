"""

DocumentString

"""

list_of_users = ["dev", "nilesh", "ramesh", "rajesh"]

for user in list_of_users:
	print(user)

print("-------------------Globals-------------------")
print(globals())


def do_something():
	print("doing something")
	return 10394

def calculate_tax(a):
	print(a)

def manage_user(b,p,a=10):
	print(a)

def mysample_fn(a):
	a()

def my_callback():
	print("I am a callback")

mysample_fn(my_callback)

do_something()
calculate_tax(100)

def my_another_function():
	def some_other_function():
		print("The Other function")
	return some_other_function

my_another_function()()

def some_function_with_params(a,b):
	print("This is function with params")
	print(a)
	print(b)

some_function_with_params(10,20)
	
print("------------------End of Application-------------------")