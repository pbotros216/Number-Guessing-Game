"""
Peter Botros 
Number gussing game 
01/15/2025
"""

# This code will run a program of guessing the number based on some questions and will be in seven attempts or under!

def computer_guess():
    print ("Think of a number between 1 and 100 BUT don't tell me!")
    input ( "Press enter when ready!!")

    lower_bound = 1
    high_bound = 100
    attempts = 0
    max_attempts = 7   # Code will use binary functions to guess the right number by asking a few questions 
 
    print("\nI will guess your number in 7 or fewer attempts.")

    while lower_bound <= high_bound and attempts < max_attempts:
        # find the mid point of the binary search  
        guess = (lower_bound + high_bound ) // 2 
        attempts += 1
        
        
        print(f"\nAttempt #{attempts}: Is your number {guess}?")
        feedback = input("Enter 'h' if my guess is too high, 'l' if it's too low, or 'c' if I guessed correctly: ").lower()

        # Input validation
        while feedback not in ['h', 'l', 'c']:
            feedback = input("Invalid input. Please enter 'h', 'l', or 'c': ").lower()

        if feedback == 'c':  # Guess is correct
            print(f"\nAyyy! I guessed your number in {attempts} attempts!")
            return
        elif feedback == 'h':  # Guess is too high
            high_bound = guess - 1
        elif feedback == 'l':  # Guess is too low
            lower_bound = guess + 1

        # Check for invalid range
        if lower_bound > high_bound:
            print("\nSomething went wrong. The range has become invalid!")
            return

    # If loop ends without finding the number
    print("\nI couldn't guess your number within 7 attempts. Are you sure you followed the rules?")

# Run the game
computer_guess()


# Explanation of the code and they key concepts  
# 	The binary search algorithm is efficient and guarantees the correct answer in  \log_2(\text{Range})  steps.
#	The program dynamically adjusts its range based on user feedback.
#	With a starting range of 100, the maximum attempts needed is  \lceil \log_2(100) \rceil = 7 .