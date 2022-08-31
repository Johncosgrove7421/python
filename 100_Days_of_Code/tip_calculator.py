
# tip calculator Python program

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give?  10, 12, or 15? "))
people = int(input("How many people to spilt the bill? "))
tip = percentage / 100
total_tip = bill * tip
total_bill = total_tip + bill
each_person = total_bill / people
total = round(each_person, 2)
print(f"Each person should pay ${total}")