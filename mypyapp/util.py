def check_null(obj):
	if obj is None:
		return True
	else:
		return False

def check_empty(obj):
	if check_null(obj) is False:
		if len(obj) is 0:
			return True
		else:
			return False
	else:
		return True
			