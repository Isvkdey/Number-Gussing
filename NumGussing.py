import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I've selected a number between 1 and 100. Can you guess it?")

    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        guess = int(input("Enter your guess (between 1 and 100): "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} correctly!")
            print(f"It took you {attempts} attempts.")
            play_again()
            return

    print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")
    play_again()

def play_again():
    play = input("Do you want to play again? (yes/no): ").lower()
    if play == "yes":
        number_guessing_game()
    elif play == "no":
        print("Thank you for playing!")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        play_again()

if __name__ == "__main__":
    number_guessing_game()
