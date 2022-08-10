#This Python program is used to calculate catering cost



print('How many people will be attending?')
p = input ('')

print('How many tables will you have?')
t = input('')

print("How many cups will the bartenders need to provide?")
c = input('')

print('How many hours will you need the bartenders for?')
h = input ('')

food = int(p) * 28 # 24 per person plus 4 for each appetizer
tablecloths = int(t) * 13
cups = int(c) * .30
bartenders = int(h) * 35

x = (food + tablecloths + cups + bartenders)

print(x+(x * .07 )) # this is the total with taxes included



# example: before taxes 
#How many people will be attending?
#60
#How many tables will you have?
#8
#How many cups will the bartenders need to provide?
#100
#How many hours will you need the bartenders for?
#4
#1954.0

# example: after taxes
#How many people will be attending?
#60
#How many tables will you have?
#8
#How many cups will the bartenders need to provide?
#100
#How many hours will you need the bartenders for?
#4
#2090.78