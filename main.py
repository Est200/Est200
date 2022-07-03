import random
print('R stands for Rock, P stands for Paper and S stands for Scissors.')
R='Rock'
P='Paper'
S='Scissors'
possible=['R','P','S']
while True:
    user_input = input("Enter a choice (R,P,S): ")
    if user_input not in possible:
    	print('Invalid. Option not available. Try again')
    	user_input= input('Enter a choice(R,P,S): ')
    possible_options = ["Rock", "Paper", "Scissors"]
    computer_action = random.choice(possible_options)
    print(f"\nYou chose {user_input}, computer chose {computer_action}.\n")

    if user_input == computer_action:
        print(f"Both players selected {user_input}. It's a tie!")
    elif user_input == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_input == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_input == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Do you want to go again? (yes/no): ")
    if play_again.lower() != "yes":
        break