import random;

user_wins = 0

computer_wins = 0

options = ["rock", "paper", "scissors"]


while True:
    input_user = input("Type Rock/ Paper/ Scissors or Q to exit the game.").lower()
    
    if input_user == 'q':
        break
    
    if input_user not in options:
        continue
    
    # Rock(0) , Paper(1), scissors(2)
    random_number = random.randint(0, 2)
    
    
    computer_pick = options[random_number]
    
    print("Computer picked", computer_pick + ".")
    
    if input_user == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
        
    elif input_user == "paper" and computer_pick == "rock":
        print("You won!") 
        user_wins += 1
        
    elif input_user == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1
        
print("You won", user_wins, "times.")
print("The Computer won", computer_wins, "times.")
print("Goodbye!")
