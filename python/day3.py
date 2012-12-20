"""Welcome to cipher day!
write a program that can encrypt texts with an alphabetical caesar cipher. This cipher can ignore numbers, symbols, and whitespace.
for extra credit, add a "decrypt" function to your program!"""

def crypt(user_string, caesar_shift):
	letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	string_length = len(user_string)
	encrypted_string = str("")
	count = 0
	while (count<string_length):
		letter_count = 0
		while (letter_count<len(letters)):
			if (user_string[count] == letters[letter_count]):
				new_letter_index = letter_count + caesar_shift
				new_letter = letters[new_letter_index]
				break;
			letter_count+=1
		encrypted_string+=new_letter
		count+=1
	return encrypted_string

while True:
	user_string = str(input("\nEnter a string to be ciphered: ")).lower()
	shift_amount = int(input("Enter a shift amount for the cipher: "))
	
	#encrypt that shit homie
	encrypted_string = crypt(user_string, shift_amount)
	print("This is your encrypted string: ",encrypted_string)
	
	#this gets negative value of integer
	shift_amount = "-" + str(shift_amount)
	shift_amount = int(shift_amount)
	
	#decrypts the string back
	decrypted_string = crypt(encrypted_string, shift_amount)
	print("This is your encrypted string decrypted", decrypted_string)