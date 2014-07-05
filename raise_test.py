
def Fail():

	try:
		1/0
	except ZeroDivisionError as e:
		raise e
	
	
try:
	Fail()
	
except ZeroDivisionError:
	print "WAZAP"