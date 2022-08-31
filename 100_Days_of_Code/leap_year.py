# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

modulo = int(year % 4)
onehun = int(year % 100)
fourhun = int(year % 400)

# print(modulo)

if modulo <= 0:
    print("Leap year.") 
elif onehun >= 0:
    print("Leap year.")
elif fourhun <= 0:
    print("Leap year.")
else:
    print("Not leap year.")