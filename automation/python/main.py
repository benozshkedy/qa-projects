# -----------------------------
# Number Guessing Game

# What this script demonstrates:
# - Clean structure (functions + main)
# - Basic input validation (try/except)
# - Clear user messages
# - Limited attempts logic
# - Optional replay
# - Optional execution time measurement

# Author: Ben Oz Shkedy
# -----------------------------

import random
import time


# ----------------------------
# Configuration (easy to change)
# ----------------------------
MIN_NUMBER = 1
MAX_NUMBER = 10
MAX_ATTEMPTS = 3  # total attempts (your original logic: 3 tries)


def print_header() -> None:
    """Print a simple game header."""
    print("\n" + "=" * 34)
    print("   Welcome to the Guessing Game")
    print("=" * 34)
    print(f"Rules: guess a number between {MIN_NUMBER} and {MAX_NUMBER}.")
    print(f"You have {MAX_ATTEMPTS} attempts.\n")


def get_int_input(prompt: str) -> int:
    """
    Ask the user for an integer input.
    Keeps asking until the user enters a valid integer.
    """
    while True:
        user_input = input(prompt).strip()
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a whole number (e.g., 7).")


def get_guess() -> int:
    """
    Ask the user for a guess within range [MIN_NUMBER, MAX_NUMBER].
    Keeps asking until the guess is valid.
    """
    while True:
        guess = get_int_input(f"Guess a number ({MIN_NUMBER}-{MAX_NUMBER}): ")
        if MIN_NUMBER <= guess <= MAX_NUMBER:
            return guess
        print(f"Out of range. Please choose between {MIN_NUMBER} and {MAX_NUMBER}.")


def build_hint(secret: int, guess: int) -> str:
    """Return a small hint message."""
    if guess < secret:
        return "Hint: try a higher number."
    return "Hint: try a lower number."


def play_round(secret_number: int) -> bool:
    """
    Play a single round.
    Returns True if the user guessed correctly, otherwise False.
    """
    attempts_used = 0

    while attempts_used < MAX_ATTEMPTS:
        attempts_used += 1
        guess = get_guess()

        if guess == secret_number:
            print(f"\nCorrect! You guessed it in {attempts_used} attempt(s).")
            return True

        remaining = MAX_ATTEMPTS - attempts_used
        print("\nWrong guess! " + build_hint(secret_number, guess))

        if remaining > 0:
            print(f"Try again. Attempts left: {remaining}\n")

    print(f"\nSorry, you've used all your tries. The correct number was {secret_number}.")
    return False


def ask_play_again() -> bool:
    """
    Ask the user if they want to play another round.
    Accepts: y/yes, n/no (case-insensitive).
    """
    while True:
        answer = input("\nPlay again? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please type 'y' or 'n'.")


def main() -> None:
    """Entry point for the program."""
    start_time = time.time()

    print_header()

    # Use a random number each round (more realistic than fixed 7)
    # If you want to keep it fixed like your original: secret_number = 7
    games_played = 0
    games_won = 0

    while True:
        games_played += 1
        secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)

        won = play_round(secret_number)
        if won:
            games_won += 1

        print("\n" + "-" * 34)
        print(f"Stats: {games_won} win(s) out of {games_played} game(s).")
        print("-" * 34)

        if not ask_play_again():
            break

    end_time = time.time()
    duration = round(end_time - start_time, 2)
    print(f"\nThanks for playing! Total session time: {duration} seconds.\n")


if __name__ == "__main__":
    main()