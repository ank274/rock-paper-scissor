#game.py

import random 
print("Rock, Paper, Scissors, Shoot!") #this is also a comment

#Capture Inputs- create a variable using input function

user_choice = input("Please choose one of the following options: 'rock', 'paper,' or scissors' (without the quotes):")
print("_________")

print("YOU CHOSE:", user_choice)

#Validate Inputs

options= ["rock", "paper", "scissors"]

# if user_choice in ["rock", "paper", "scissors"]:
#     pass
    # print("Valid")
# else:
if user_choice not in options: 
    print("Invalid selection, please try again")
    exit() 
#Generate Computer Selection

print("Generating...")

computer_choice = random.choice(options) 

print("_________")
print("Generating...")
print("computer_choice:", computer_choice)

#Determine the Winner

#rock beats scissors
#paper beats rock
#scissors beats paper
# same selections is a tie

# if user_choice == computer_choice:
#     print("TIE")
    
# elif user_choice == "rock" and computer_choice == "paper":
#     print ("WINNER IS PAPER")
# elif user_choice == "rock" and computer_choice == "scissors":
#     print ("COMPUTER WINS")

# elif user_choice == "paper" and computer_choice == "rock":
#     print ("PAPER")
# elif user_choice == "paper" and computer_choice == "scissors":
#     print ("SCISSORS")

# elif user_choice == "scissors" and computer_choice == "rock":
#     print ("ROCK")
# elif user_choice == "scissors" and computer_choice == "paper":
#     print ("SCISSORS")
    
winners = {
    "rock":{
        "rock": None,
        "paper": "paper",
        "scissors": "rock",
    },
    "paper":{
        "rock": "paper",
        "paper": None,
        "scissors": "scissors",
    },
    "scissors":{
        "rock": "rock",
        "paper": "scissors",
        "scissors": None,
    },
}

winning_choice = winners[user_choice][computer_choice]


#Display Final Outputs/ Outcomes 
if winning_choice:
    if winning_choice == user_choice:
        print("YOU WON")
    elif winning_choice == computer_choice:
        print("YOU LOST")
else:
    print("TIE")

print("Thanks for playing. Please play again!")