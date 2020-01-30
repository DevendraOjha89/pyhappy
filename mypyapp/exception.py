try:
	open("c:/somefile123.pdf")

except FileNotFoundError:
	print("No Such File")
finally:
	print("finally")


	