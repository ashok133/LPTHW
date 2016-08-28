from sys import argv

script,  uname = argv

prompt = '> '

print "Hi %s, I'm the %s script." %(uname,script)
print "I'd like to ask you a few questions."
print "Do you like me? "
likes = raw_input(prompt)
print "Where do you live", uname
address = raw_input(prompt)
print "What kind of a computer do you have? "
type = raw_input(prompt)

print """
Alright %s, so you said %s about liking me.
You live in %s. Not sure where that is.
And you have a %r computer. Nice.
""" %(uname, likes, address, type) 