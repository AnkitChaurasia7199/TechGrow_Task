import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    guess = None

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while guess != number_to_guess:
        guess = int(input("Enter your guess: "))

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the correct number.")
    
    input("Press Enter to exit...")

guess_number()
