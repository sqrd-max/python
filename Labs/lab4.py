# # Task 1
# # Prompt the user to enter a number
# number_input = input("Enter a number: ")
#
# # Attempt to convert the input to an integer
# try:
#     number = int(number_input)
#     # Check if the number is even
#     if number % 2 == 0:
#         print(f"The entered number {number} is even.")
#     else:
#         print("The number is not even.")
# except ValueError:
#     print("Invalid input. Please enter an integer.")

# Task 2
# Create an empty dictionary to store the responses
# responses = {}
#
# # Ask questions and collect responses
# responses['Name'] = input("What is your name? ")
# responses['Position'] = input("Which position are you applying for? ")
# responses['Experience'] = input("How many years of experience do you have in this field? ")
# responses['Reason'] = input("Why do you want to work with us? ")
# responses['Expectation'] = input("What are your salary expectations? ")
#
# # Display the collected data at the end
# print("\nCollected Interview Data:")
# for question, response in responses.items():
#     print(f"{question}: {response}")


# # Task 3
# # Initialize a variable for the sum
# sum_for = 0
#
# # Use a for loop to calculate the sum
# for i in range(1, 101):  # range(1, 101) generates numbers from 1 to 100
#     sum_for += i
#
# # Print the result
# print(f"The sum of numbers from 1 to 100 is {sum_for}.")
#
#
# # Initialize variables for the sum and iterator
# sum_while = 0
# i = 1
#
# # Use a while loop to calculate the sum
# while i <= 100:
#     sum_while += i
#     i += 1
#
# # Print the result
# print(f"The sum of numbers from 1 to 100 is {sum_while}.")


# Task 4
def check_winner(player1, player2):
    """Determine the game winner."""
    if player1 == player2:
        return "It's a tie!"
    elif (player1 == "Rock" and player2 == "Scissors") or \
            (player1 == "Scissors" and player2 == "Paper") or \
            (player1 == "Paper" and player2 == "Rock"):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"


def play_game():
    """Play a game of Rock, Paper, Scissors."""
    while True:
        # Collect players' choices
        player1_choice = input("Player 1, enter your choice (Rock, Paper, Scissors): ")
        player2_choice = input("Player 2, enter your choice (Rock, Paper, Scissors): ")

        # Check and print the winner
        result = check_winner(player1_choice, player2_choice)
        print(result)

        # Ask if the players want to start a new game
        new_game = input("Do you want to start a new game? (yes/no): ")
        if new_game.lower() != "yes":
            print("Thanks for playing!")
            break


# Start the game
play_game()
