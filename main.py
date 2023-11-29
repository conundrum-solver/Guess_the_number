import random
from art import logo
print(logo)

print("Welcome to the game where you read my mind.\nI'm thinking of a number between 1 and 100.")

difficulty=input("Choose a difficulty 'easy' or 'hard': ")
starting_guesses=0
if difficulty=="easy":
    starting_guesses=10
elif difficulty=="hard":
    starting_guesses=5

random_number=random.randint(1,100)
print(f"the number is {random_number}")
game_on=True
def guess_the_number():
    guesses_left = starting_guesses
    while game_on:

        if guesses_left == 0:
            return print("You ran out of guesses. You lose!")

        print(f"You have {guesses_left} guesses left")

        player_guess=int(input("Guess the number: "))

        if player_guess > random_number:
            print("Too high")
            guesses_left -=1

        elif player_guess < random_number:
            print("Too low")
            guesses_left -= 1

        elif player_guess == random_number:
            return print(f"You guessed right! The number is {random_number}")

guess_the_number()
play_again=input("Do you want to play again? Yes or No: ")
if play_again=="Yes":
    guess_the_number()