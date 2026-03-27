"""
Peter Botros
Number Guessing Game (Binary Search)
01/15/2025
"""

# This program guesses the user's number using a binary search strategy
# within 7 attempts or fewer.

def computer_guess():
    print("Think of a number between 1 and 100 (don’t tell me!)")
    input("Press Enter when you're ready...")

    lower_bound = 1
    high_bound = 100
    attempts = 0
    max_attempts = 7

    print("\nI will guess your number in 7 or fewer attempts.")

    while lower_bound <= high_bound and attempts < max_attempts:
        guess = (lower_bound + high_bound) // 2
        attempts += 1

        print(f"\nAttempt #{attempts}: Is your number {guess}?")
        feedback = input("Enter 'h' (too high), 'l' (too low), or 'c' (correct): ").lower()

        while feedback not in ['h', 'l', 'c']:
            feedback = input("Invalid input. Enter 'h', 'l', or 'c': ").lower()

        if feedback == 'c':
            print(f"\nI guessed your number in {attempts} attempts!")
            return
        elif feedback == 'h':
            high_bound = guess - 1
        else:
            lower_bound = guess + 1

        if lower_bound > high_bound:
            print("\nInvalid responses detected. Please follow the rules.")
            return

    print("\nI couldn't guess your number within 7 attempts.")

computer_guess()




# Explanation:
# This program uses a binary search algorithm to efficiently guess a number between 1 and 100.
# Binary search reduces the possible range by half after each guess.
# Because log2(100) ≈ 7, the program guarantees finding the number in 7 attempts or fewer. 
