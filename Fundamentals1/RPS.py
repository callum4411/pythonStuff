import random

def get_random_choice():
    random_number = random.randint(1, 3)
    return random_number

# returns a text choice based on a number choice (Rock-1, Paper-2, Scissors-3)
def get_text_choice(num_choice):
    if num_choice == 2:
        return "Paper"
    elif num_choice == 1:
        return "Rock"
    else:
        return "Scissors"


# returns the computer's choice in text format
def get_computer_choice(num_choice):
    if num_choice == 2:
        return "Paper"
    elif num_choice == 1:
        return "Rock"
    else:
        return "Scissors"




def get_winner(player, computer):
    if player == computer:
        return "tie"
    if (player == "Rock" and computer == "Scissors") or (player == "Scissors" and computer == "Paper") or (player == "Paper" and computer == "Rock"):
        return "you"
    else:
        return "computer"

# plays a single game and allows for user input to enter a choice
def play_a_game():
    player = get_text_choice(int(input("chose between 1 2 and 3 for Rock, Paper or Scissors respectively: ")))
    computer = get_text_choice(get_random_choice())
    print(player + " vs " + computer)
    if get_winner(player, computer) == "you":
        print("You win with " + player)
    elif get_winner(player, computer) == "computer":
        print("Computer win's with " + computer)
    else:
        print("Tie")

# allows for user input to play multiple games
def main():
    playAgain = True
    pc = "y"
    while playAgain:
        play_a_game()
        pc = input("Do you want to play again? (y/n): ")
        if pc == "y":
            playAgain = True
        else:
            playAgain = False
            print("Thank you for playing")
            break


# Start the game
main()