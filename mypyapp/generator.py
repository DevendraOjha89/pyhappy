def myfunction():
	a = 10
	yield a

	print("doing work")
	print("doing further work")

	a = 20
	yield a

	print("doing further work")
	print("doing more further work ")
	a = 30
	yield a

iter = myfunction()
print(iter.__next__())