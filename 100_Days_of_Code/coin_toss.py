import random
print("Welcome to the coin toss generator! ")

input("We'll flip for it, call it, Heads or Tails???  ")
toss = random.randint(0,1)
if toss == 0:
    print("HEADS!")
if toss == 1:
    print("TAILS!")

