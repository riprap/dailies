"""
create a program that will ask the users name, age, and reddit username. have it tell them the information back, in the format:
your name is (blank), you are (blank) years old, and your username is (blank)
for extra credit, have the program log this information in a file to be accessed later.
"""
name =input("Enter your name: ")
age = input("Enter your age: ")
username = input("Enter your reddit username: ")
save_string = "your name is %s, you are %s years old, and your username is %s." %(name, age, username)

print(save_string)

save_file = open('txt/day1.txt', 'a')
save_file.write("%s\n" % save_string)
save_file.close()