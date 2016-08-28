from sys import *

def gold_room():
	print "This room is full of gold.\n How much would you take?"
	how_much = int(raw_input("> "))
	if how_much < 50:
		print "You aren't greedy. You win!"
	else:
		print "You greedy bastard!"


def start():
	print "You are in a dark room.\nThere is a door to your right and left.\nWhich one do you take?"
	choice = raw_input("> ")

	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you die.")

def dead(str):
	print str, "Good job!"
	exit(0)

def bear_room():
	bear_moved = False
	print "There's a bear here.\n The bear has a bunch of honey.\nThe fat bear is in front of another door.\nHow are you going to move the bear? "

	while True:
		choice = raw_input("> ")

		if choice == "take honey":
			dead("The bear looks at you and slaps your face off")
		elif choice == "taunt bear" and not bear_moved:
			print("The bear has moved from the door and you can go through it now.")
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif choice == "open door" and bear_moved:
			gold_room()
		else: 
			print "No clue what that means."

def cthulhu_room():
	print "Here you encounter the greatest evil Cthulhu.\n He, it, whatever stares at you and you go insane.\nDo you flee for life or eat your head?"
	choice = raw_input("> ")

	if "flee" in choice:
		print "You flee for life back into the dark room. Wanna continue ?"
		continue1 = raw_input("> ")

		if continue1 == "Y" or continue1 == "Yes":
			print "Great."
			start()
	
		else:
			print "Thanks for visiting!"
			exit(0)
	
	elif "head" in choice:
		print "That was tasty. You don't exist anymore."
		exit(0)

	else:
		print "Well, that's not an option. Let's do it again."
		cthulhu_room()


start()

