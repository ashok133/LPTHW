def add(a,b):
	print "Adding %d and %d gives %d" %(a,b,a+b)
	return a + b 

def subtract(a,b):
	print "Subtracting %d from %d gives %d"%(a,b,a-b)
	return a - b 

def multiply(a,b):
	print "%d times %d gives %d"%(a,b,a*b)
	return a*b

def divide(a,b):
	print "%d divided by %d gives %d" %(a,b,a/b)
	return a/b

def power(a,b):
	print "%d raised to power of %d gives "%(a,b)
	return a**b 

print "Let's do some math with just functions"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"