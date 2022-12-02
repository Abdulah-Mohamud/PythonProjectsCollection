import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to Rock, Paper or Scissors")
print("--------------------------------------")

player_choice = input("Please select from rock, paper or scissors? ")

if player_choice == "rock":
  player_choice = 1
elif player_choice == "paper":
  player_choice = 2
else:
  player_choice = 3

computer_choice = random.randint(0,2)

row1 = ["draws","wins","loses"]
row2 = ["loses","draws","wins"]
row3 = ["wins","loses","draws"]
map = [row1, row2, row3]

#1 - Rock, 2 - Paper, 3- scissors
if player_choice == 1:
  print(rock)
elif player_choice == 2:
  print(paper)
else:
  print(scissors)

if computer_choice == 0:
  print(rock)
elif computer_choice == 1:
  print(paper)
else:
  print(scissors)

outcome = map[computer_choice][player_choice - 1]
print(f"The player {outcome} this round")
