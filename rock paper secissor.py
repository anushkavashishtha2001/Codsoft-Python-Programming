import random

def get_user_choice():
    
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        print("Invalid input. Please try again!")

def get_computer_choice():
   
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    print(f"Your choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    print(result)

def play_multiple_rounds():
    
    user_score = 0
    computer_score = 0

    while True:
        play_game()
        result = determine_winner(get_user_choice(), get_computer_choice())
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}")
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again!= 'y':
            break

def main():
    print("Welcome to Rock-Paper-Scissors!")
    play_multiple_rounds()

if __name__ == "__main__":
    main()