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
        mass = float(input("Enter Mass: "))
        acceleration = float(input("Enter Acceleration: "))
        force = mass*acceleration
        print("Force = ", force)
        
    elif(solve_for == "M"):
        print ("\nM = F / A")
        force = float(input("Enter Force: "))
        acceleration = float(input("Enter Acceleration: "))
        mass = force/acceleration
        print("Mass = ", mass)
    
    elif (solve_for == "A"):
        print ("\nA = F / M")
        force= float(input("Enter Force: "))
        mass = float(input("Enter Mass: "))
        acceleration = force / mass
        print("Acceleration = ", acceleration)