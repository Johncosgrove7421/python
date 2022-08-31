# Based on a user's order, work out their final bill.

# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

# Example Input
# size = "L"
# add_pepperoni = "Y"
# extra_cheese = "N"
# Example Output
# Your final bill is: $28.
print("Welcome to Python Pizza Deliveries! ")

size = input("What size pizza do you want? S, M, or L ")
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25

add_pepperoni = input("Do you want pepperoni? Y or N ")
if size == "S":
    if add_pepperoni == "Y":
        bill += 2
else:
    bill += 0

if size == "M":
    if add_pepperoni == "Y":
        bill += 3
else:
    bill += 0
if size == "L":
    if add_pepperoni == "Y":
        bill += 3
else:
    bill += 0

extra_cheese = input("Do you want extra cheese? Y or N ")
if extra_cheese == "Y":
    bill += 1
else:
    bill += 0
print(f"Your final bill is: ${bill}.")

