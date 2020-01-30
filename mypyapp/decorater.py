

def decofn(target): #poincut
	def decologic(): #advice
		print("Before Method")
		result = target() #invoking the actual target method
		print("After method")
		return result # the proxy should not swallow any result and my expectation
	return decologic

@decofn
def function():
	print("business logic")
	return 1000


print(function())