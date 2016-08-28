from sys import argv

script, filename = argv

print "We will eare %r" %filename
print "If you don't want that, hit ^C"
print "If you do want that, hit RETURN."

raw_input("? ");

print "Opening the file..."
target = open(filename, 'w')

print ("truncating %r") %filename
print "Goodbye!"

target.truncate()

print "Enter your own text to be written in the file:"

string1 = raw_input()

print ("Writing the file...")

target.write(string1)

print "Let's close %r" %filename
target.close()
print "Closed."


print "Let's check what we've written."

target2 = open(filename)
print target2.read()

target2.close()
