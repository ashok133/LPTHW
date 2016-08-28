the_count = [1,2,3,4,5]

fruits = ['apples', 'oranges','pears', 'apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

for number in the_count:
	print "This is count %d" %number

for fruit in fruits:
	print "We have %s " %fruit

for i in change:
	print "I've got %r" %i

print "Let's make a new list"

elements = []

for i in range(1,6):
	elements.append(i)
	print "Element added: %d" %i

print "Here's the list we just created."

print str(elements).strip(' ')

print "Here's a previous list: \nFruits - ",
print ", ".join(fruits)

