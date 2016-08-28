tabby_cat =  "\tI'm tabbed in."
persian_cat = "I'm split\non a line\r"
backslash_cat = "I'M \\ A \\ CAT"

fat_cat = '''
I'll do a list: 
\t* Cat foods \r\r\r
\t* Fishies 
\t* Catnip\n\t* Grass
'''

print "%r " %tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#%r will not escape your characters for you, it'll print out the string as is.


