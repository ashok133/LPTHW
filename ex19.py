def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" %cheese_count
	print "you have %d boxes of crackers!" %boxes_of_crackers

cheese_and_crackers(20,30)

print "How many cheeses do you think you have?"
cheese_no = int(raw_input())

print "And how many boxes of crackers? "
cracker_no = int(raw_input())

cheese_and_crackers(cheese_no,cracker_no)
cheese_and_crackers(10+20, 30+40)
cheese_and_crackers(cheese_no+10, cracker_no+20)
