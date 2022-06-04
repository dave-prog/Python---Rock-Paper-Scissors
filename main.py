# import random module
import random

#makes the whole program a loop, so the game can be played continously
while True:
    #store possible outcomes in list
    possible_outcomes = ["R", "P", "S"]

    # Takes user input
    user_action = input("Enter a choice (R, P, S): ")
    while user_action not in possible_outcomes:
        user_action = input("That is not a valid choice. Please try again: ")

    
    #Computer makes choice
    computer_action = random.choice(possible_outcomes)

    
    #print out user and computer's choice
    print(f"\nPlayer({user_action}) : CPU({computer_action})\n")
    
    
    #compute all possibilities and prints out the results
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "R":
        if computer_action == "S":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "P":
        if computer_action == "R":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "S":
        if computer_action == "P":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break