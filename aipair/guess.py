import random


def play_game():
    """Play a number guessing game with three valid guesses."""
    number = random.randint(1, 15)
    guesses_used = 0

    print("I'm thinking of a number from 1 to 15. You have 3 guesses.")

    while guesses_used < 3:
        try:
            guess = int(input("Enter your guess: ").strip())
        except ValueError:
            print("Please enter a whole number.")
            continue

        if not 1 <= guess <= 15:
            print("Your guess must be between 1 and 15.")
            continue

        guesses_used += 1
        if guess == number:
            print("Correct! You guessed the number.")
            return

        if guess < number:
            print("Too low.")
        else:
            print("Too high.")

    print(f"Out of guesses! The number was {number}.")


if __name__ == "__main__":
    play_game()