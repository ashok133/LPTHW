from sys import argv

script, filename = argv

txt = open(filename)

print "filen to be opened: %r" %filename
print txt.read()

print "What file should I open now? "
file2 = raw_input("> ")

txt2 = open(file2)

print "Here's your file: "

print txt2.read()

txt2.close()
txt.close()

