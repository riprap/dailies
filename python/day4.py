"""
You're challenge for today is to create a random password generator!
For extra credit, allow the user to specify the amount of passwords to generate.
For even more extra credit, allow the user to specify the length of the strings he wants to generate!
"""
import random

class Password:
	def __init__(self, length):
		self.password = self.generate_random(length)
	
	def generate_random(self,password_length):
		password=""
		count = 0
		#only ascii characters between 33 and 127 display
		#so we will limit it to those
		range_min = 33
		range_max = 127
		while count < password_length:
			password += chr(random.randint(range_min,range_max))
			count+=1
		return password
	
	def get_password(self):
		return self.password

if __name__=="__main__":
	number_passwords = int(input("How many random passwords do you want? (1-24) "))
	length_password = int(input("How long do you want the random password to be?"))
	if number_passwords > 0 and number_passwords < 25:
		count = 1
		while count <= number_passwords:
			password = Password(length_password)
			print "password #%s: %s" % (count, password.get_password())
			count+=1