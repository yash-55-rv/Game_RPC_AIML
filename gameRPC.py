import random

def play_rock_paper_scissors():
    """
    Plays a game of rock, paper, scissors against the computer.
    Keeps score until the user chooses to exit.
    """
    player_score = 0
    computer_score = 0
    options = ['rock', 'paper', 'scissors']

    print("Welcome to Rock, Paper, Scissors!")
    print("---------------------------------")
    print("Type 'exit' at any time to quit the game.")
    print("---------------------------------")

    # The game loop continues until the user chooses to exit
    while True:
        # Get user input and convert to lowercase for consistent comparison
        player_choice = input("Enter your choice (rock, paper, scissors): \nenter exit for leaving the game\n").lower()

        # Check for the exit condition
        if player_choice == 'exit':
            print("\nThanks for playing!")
            break

        # Validate user input
        if player_choice not in options:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            continue

        # Generate a random choice for the computer
        computer_choice = random.choice(options)
        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}\n")

        # Determine the winner and update scores
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            print("You win this round!")
            player_score += 1
        else:
            print("You lose this round!")
            computer_score += 1

        # Print the current score
        print(f"Current Score: You: {player_score} | Computer: {computer_score}\n")

    # Print final score when the game ends
    print("---------------------------------")
    print("Final Score:")
    print(f"You: {player_score} | Computer: {computer_score}")
    print("---------------------------------")

if __name__ == "__main__":
    play_rock_paper_scissors()
