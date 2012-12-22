"""
we all know the classic "guessing game" with higher or lower prompts. lets do a
role reversal; you create a program that will guess numbers between 1-100, and
respond appropriately based on whether users say that the number is too high or
too low. Try to make a program that can guess your number based on user input 
and great code!
"""
import random
#holds all the guesses
guesses = [0,101]
guesses_result = [1,0]

def next_guess(guesses_list, guesses_result_list):
    higher_list = []
    lower_list = []
    count = 0
    while count < len(guesses_list):
        if guesses_result_list[count] == 0:
            lower_list.append(guesses_list[count])
        elif guesses_result_list[count] == 1:
            higher_list.append(guesses_list[count])
        count+=1
    
    print higher_list
    print lower_list
    
    bottom_range = max(higher_list)+1
    top_range = min(lower_list)-1
    next_guess = random.randint(bottom_range, top_range)
    return next_guess

guess = False

while guess == False:
    guess_number = next_guess(guesses, guesses_result)
    user_input = raw_input("Is this your number(enter correct, higher, or lower: %i\n"%guess_number)
    user_input.lower()
    
    if user_input == "correct":
        print "I knew I'd get it eventually"
        guess = True
    elif user_input == "higher":
        guesses.append(guess_number)
        guesses_result.append(1)
    elif user_input == "lower":
        guesses.append(guess_number)
        guesses_result.append(0) 
    else:
        print "You idiot, that's not one of the accepted words."