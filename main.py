#WELCOME MSG
#random function
#how much attempts
#while loop
#if else condition
#congratulation
#next time
#lower number
#greater number



import random

print("WELCOME TO THE NUMBER GUESSING GAME")

# Generate a random number between 50 and 100
random_number = random.randint(50, 100)

# Define maximum attempts
guess_chances = 5
count_start = 0

while count_start < guess_chances:
    my_guess = int(input("Enter any number: "))

    count_start += 1  # Increase attempt count

    if my_guess == random_number:
        print(f"Congratulations! 🎉 You guessed the right number {random_number} in {count_start} attempts.")
        break
    elif my_guess < random_number:
        print("Your guess is too low. Try a higher number!")
    elif my_guess > random_number:
        print("Your guess is too high. Try a lower number!")

    # Check if this was the last attempt
    if count_start == guess_chances:
        print(f"Oops, you've used all {guess_chances} attempts! The correct number was {random_number}. Better luck next time!")

