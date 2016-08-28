def print_two(*args):
	args1, args2 = args
	print "arg1: %r \narg2: %r" %(args1,args2)

def print_two_again(args1,args2):
	print "arg1: %r \narg2: %r" %(args1,args2)

def print_one(args1):
	print "arg1: %r " %(args1)

def print_none():
	print "I got nothin'!"

print "Enter your first name: "
f_name = raw_input()

print "Enter your last name: "
l_name = raw_input()

print_two(f_name,l_name)
print_two_again(f_name,l_name)
print_one(f_name)
print_none()
