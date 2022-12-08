import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

display = []
word_length = len(chosen_word)
for _ in range(word_length):
 display += "_"
print(display)
lives = 6
game_over = False
while not game_over:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if letter != guess:
        lives -= 1
    print(f"You have {lives} remaining")

    print(display)

    if "_" not in display:
        game_over = True
        chosen_word2 = ''.join(display)
        print(f"Player Won, the final work was {chosen_word2}")
