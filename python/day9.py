"""
write a program that will allow the user to input digits, and arrange them in numerical order.
for extra credit, have it also arrange strings in alphabetical order
"""
numbers=[]
strings=[]
run = True

while run == True:
	print "Enter q to quit"
	user_input = raw_input("Enter a number or a string-->")
	
	try:
		#can we turn it into a float?
		user_input = float(user_input)
	except:
		#if not lets keep it as a string
		user_input = str(user_input)
	
	if user_input == "q" or user_input == "Q":
		run = False
		
	elif isinstance(user_input,str):
		strings.append(user_input)
		
	elif isinstance(user_input,float):
		numbers.append(user_input)

numbers.sort()
strings.sort()
print "Integers in order: %s" %numbers
print "Strings in alphabetical order: %s" %strings