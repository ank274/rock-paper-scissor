#game.py

import random 
print("Rock, Paper, Scissors, Shoot!") #this is also a comment

#Capture Inputs- create a variable using input function

user_choice = input("Please choose one of the following options: 'rock', 'paper,' or scissors' (without the quotes):")
print("_________")

print("YOU CHOSE:", user_choice)

#Validate Inputs


if user_choice in ["rock", "paper", "scissors"]:
    pass
    # print("Valid")
else:
    print("Invalid selection, please try again")
    exit() 
#Generate Computer Selection

print("Generating...")

computer_choice = random.choice(["rock", "paper", "scissors"])

print("_________")
print("Generating...")
print("computer_choice:", computer_choice)

#Determine the Winner

#Display Final Outputs/ Outcomes 