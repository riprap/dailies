"""
Hello, coders! An important part of programming is being able to apply your programs, so your 
challenge for today is to create a calculator application that has use in your life. It might be an 
interest calculator, or it might be something that you can use in the classroom. For example, if 
you were in physics class, you might want to make a F = M * A calc.
EXTRA CREDIT: make the calculator have multiple functions! Not only should it be able to 
calculate F = M * A, but also A = F/M, and M = F/A!
"""

while True:
    solve_for = input("What do you want to solve for? (F, M, or A)").upper()
    
    if (solve_for == "F"):
        print ("\nF = M * A")
        mass = input("Enter Mass: ")
        acceleration = input("Enter Acceleration: ")
        force = float(mass)*float(acceleration)
        print("Force = ", force)
        
    elif(solve_for == "M"):
        print ("\nM = F / A")
        force = input("Enter Force: ")
        acceleration = input("Enter Acceleration: ")
        mass = float(force)/float(acceleration)
        print("Mass = ", mass)
    
    elif (solve_for == "A"):
        print ("\nA = F / M")
        force= input("Enter Force: ")
        mass = input("Enter Mass: ")
        acceleration = float(force) / float(mass)
        print("Acceleration = ", acceleration)