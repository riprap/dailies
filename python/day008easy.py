"""
write a program that will print the song "99 bottles of beer on the wall".
for extra credit, do not allow the program to print each loop on a new line.
"""
import time
bottles = 99

while bottles > 0:
	if bottles != 0:
		print "%i bottles of beer on the wall, %i bottles of beer." %(bottles, bottles)
		bottles-=1
		
		if bottles == 0:
			print "Take one down and pass it around, no more bottles of beer on the wall."
			print "No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall."
	
		else:
			print "Take one down and pass it around, %i bottles of beer on the wall." % bottles