"""
This program shows IMPORT statements nad LOOPS
"""

# IMPORT statements first.
import random

random.randint(1,100)

ans = random.randint(1,100)

while (ans == True):
        
    print ("Guess the number between 1 and 100.")
        
    guess = int(input("Guess: "))
        
    if guess > ans :
        print ("This number is too high!")
        continue
    if guess < ans :
        print ("This number is too low...")
        continue
    if guess == ans :
        print ("You got it!")
        break
    elif ans > 100 or ans <1 :
        print 
        

