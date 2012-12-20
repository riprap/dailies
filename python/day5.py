""" 
Your challenge for today is to create a program which is password protected, and wont open unless the correct user and password is given.
For extra credit, have the user and password in a seperate .txt file.
for even more extra credit, break into your own program :)
"""
import re
import getpass

def get_file_contents():
	f = open('txt/day5.txt', 'r')
	file_contents = f.read()
	f.close()
	return file_contents
	
def get_user_pass(file_content):
	find_user_pass = r"""^u: (.*?) p: (.*?)$"""
	user_pass = re.compile(find_user_pass).findall(file_content)
	return user_pass[0]
	
def print_welcome(username):
	return "Log in Successful\n-------------------\nWelcome back to your file, %s" % username

print "Log-in to view file"
logged_in = False
login_attempt = 0
login_attempts_allowed = 3

while logged_in == False and login_attempt < login_attempts_allowed:
	input_user = str(raw_input("User: "))
	input_pass = str(getpass.getpass("Pass: "))

	content = get_file_contents()
	user_pass = get_user_pass(content)
	user = str(user_pass[0])
	password = str(user_pass[1])

	if input_user == user and input_pass == password:
		print print_welcome(user)
		logged_in = True

	else:
		login_attempt += 1
		print "\nInvalid log in attempt #%s\nTry Again" % login_attempt