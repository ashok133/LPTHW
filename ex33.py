i = 0
numbers = []

while i < 6: 
	print "At the top i is %d " %i
	numbers.append(i)
	i += 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d\n" %i

print "The numbers: "
print str(numbers)

#Study Drill

numbers2 = []

def while_call(number):
	print "Number input: %d" %number
	i = 0
	while i < number:
		numbers2.append(i)
		print "List so far:", str(numbers2)
		i+=1
		 

print "How long should the list be? "
number = input()
while_call(number)

while i < number:
		numbers2.append(i)
		print "List so far:", str(numbers2)