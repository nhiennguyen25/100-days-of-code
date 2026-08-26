import random
import art

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
random_number = random.randint(1,100)

easy_or_hard = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if easy_or_hard == "easy":
    attempts = 10
elif easy_or_hard == "hard":
    attempts = 5

playing_game = True
while playing_game:
    print(f"You have {attempts} attempts remaining to guess the number.")

    guess = int(input("Make a guess: "))

    if guess < random_number:
        attempts -= 1
        print("Too low")
    elif guess > random_number:
        attempts -= 1
        print("Too high")
    elif guess == random_number:
        playing_game = False
        print(f"You got it! The answer was {random_number}.")

    if attempts == 0:
        playing_game = False
        print("You ran out of guesses! Refresh the page to play again 😜")
    elif guess != random_number:
        print("Guess again.")