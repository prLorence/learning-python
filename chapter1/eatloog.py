eggAmount = int(input("Please how much eggs you're going to buy: "))

oneEgg = 1
oneDozen = 12
oneEggPrice = 7
oneDozenPrice = 70
finalPrice = 0

if eggAmount < 12:
  finalPrice = oneEggPrice * eggAmount
elif eggAmount == 12: 
  finalPrice = 70
else:
  moreThanOneDozen = divmod(eggAmount, oneDozen)
  oneDozenFromInput = moreThanOneDozen[0] * oneDozenPrice
  oneEggFromInput = moreThanOneDozen[1] * oneEggPrice
  finalPrice = oneDozenFromInput + oneEggFromInput


print(finalPrice)
