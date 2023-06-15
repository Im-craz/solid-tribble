import random


exit = False
user_points = 0
computer_points = 0

while exit == False:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, scissors or exit: ")
    user_input = user_input.lower()
    computer_input = random.choice(options)

    valid_input = ("rock", "paper", "scissors", "exit")

    if user_input not in valid_input:
        print("Invalid input")

    if user_input == "exit":
        print("Game ended")
        print(f"You won a total score of {user_points} and the computer total score is {computer_points}")
        exit = True

    if user_input == "rock":
        if computer_input == "rock":
            print("Your input is rock")
            print("Computer input is rock")
            print("It is a tie!")
        elif computer_input == "paper":
            print("Your input is rock")
            print("Computer input is paper")
            print("Computer wins")
            computer_points += 1
        elif computer_input == "scissors":
            print("Your input is rock")
            print("Computer input is scissors")
            print("You win")
            user_points += 1

    elif user_input == "paper":
        if computer_input == "rock":
            print("Your input is paper")
            print("Computer input is rock")
            print("You win!")
            user_points += 1
        elif computer_input == "paper":
            print("Your input is paper")
            print("Computer input is paper")
            print("It's a tie!")
        elif computer_input == "scissors":
            print("Your input is paper")
            print("Computer input is scissors")
            print("Computer wins")
            computer_points += 1

    elif user_input == "scissors":
        if computer_input == "rock":
            print("Your input is scissors")
            print("Computer input is rock")
            print("Computer win")
            computer_points += 1
        elif computer_input == "paper":
            print("Your input is scissors")
            print("Computer input is paper")
            print("You win!")
        elif computer_input == "scissors":
            print("Your input is scissors")
            print("Computer input is scissors")
            print("It's a tie!")
