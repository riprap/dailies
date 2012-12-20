"""
we all know the classic "guessing game" with higher or lower prompts. lets do a role reversal; you create a program that will guess numbers between 1-100, and respond appropriately based on whether users say that the number is too high or too low. Try to make a program that can guess your number based on user input and great code!
"""
#holds all the guesses
guesses = [(101,0), (0,1)]

def record_guess(guess_number,higher_lower,guesses_array):
	if higher_lower == "higher":
		guesses_array = guesses_array + (guess_number,1)
	elif higher_lower == "lower":
		guesses_array = guesses_array + (guess_number,0)
	return sorted(guesses_array)
	
def next_guess():
	count = 0
	amount = len(guesses)
	while count < amount:
		print guesses[count]
		count+=1
	next_guess = 2
	return next_guess




guess = False

while guess == False:
	guess_number = next_guess()
	user_input = raw_input("Is this your number%i"%guess_number)
	user_input.lower()
		
	if user_input == "correct":
	 	print "I knew I'd get it eventually"
		guess = True
	else:
		guesses = record_guess(guess_number, user_input, guesses)