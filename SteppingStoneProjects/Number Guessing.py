import random

print("Welcome to the guessing game")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty between easy and hard?:")

if difficulty == "easy":
    lives = 10
else:
    lives = 5

def game(lives):
    computer_guess = random.randint(1, 101)
    print(f"the number is {computer_guess}")
    lives_left = lives
    game_over = False
    while not game_over:
        print(f"You have {lives_left} lives left")
        user_guess = int(input("Guess a number between 1 and 100: "))
        if user_guess == computer_guess:
            game_over = True
            print("Well done, You have guessed correctly")
        elif user_guess > computer_guess:
            lives_left -= 1
            print("Your guess is too high")
        else:
            lives_left -= 1
            print("Your guess is too low")
        if lives_left == 0:
            game_over = True
            print("You ran out lives, you lost the game")


game(lives)
play_on = input("Would you like to play again? 'y' or 'n'?")

if play_on == "y":
    game(lives)
else:
    print("Thank you for playing")
