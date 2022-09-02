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
game = [rock, paper, scissors]
name = input("What is your name??  ")
human = int(input(" What do you choose, Type 0 for Rock, 1 for Paper or 2 for scissors "))

if human == 0:
    print(game[0])
elif human == 1:
    print(game[1])
else:
    print(game[2])

# All the different scenarios 
computer = random.randint(0, 2)


if human == computer:
    print("It's a tie")
if human == 0 and computer == 1:
    print(f"You lose {name}! ")
if human == 1 and computer == 0:
    print(f"You win {name}! ")
if human == 1 and computer == 2:
    print(f"You lose {name}! ")
if human == 2 and computer == 1:
    print(f"You win {name}! ") 
if human == 0 and computer == 2:
    print(f"You lose {name}! ")
if human == 2 and computer == 0:
    print(f"You lose {name}! ")
    
 
 
print(game[computer])

