# ask for the inputs
# add all inputs
# if total is >= 50, apply 25% discount and take 10% for the rental. 
# else do the computation with only 10% deduction 
# rawPrice = target donation - total order price

targetDonation = float(input("Please enter your target donation: "))
puzzleInput = float(input("Please enter how many puzzles: "))
talkingDollsInput = float(input("Please enter how many talking dolls: "))
teddyBearsInput = float(input("Please enter how many teddy bears: "))
pokemonInput = float(input("Please enter how many pokemon plushies: "))
toyTruckInput = float(input("Please enter how many toy trucks: "))

puzzle = 14.0
talkingDoll = 3.0
teddyBear = 20.2
pokemonPlushies = 8.20
toyTruck = 10.65

totalOrders = puzzleInput + talkingDollsInput + teddyBearsInput + pokemonInput + toyTruckInput

totalOrderPrice = (puzzleInput * puzzle) + (talkingDollsInput * talkingDoll) + (teddyBearsInput * teddyBear) + (pokemonInput * pokemonPlushies) + (toyTruckInput * toyTruck)

if totalOrders >= 50:
  discount = totalOrderPrice * 0.25
  discountPrice = totalOrderPrice - discount

  rawPrice = discountPrice - targetDonation

  rentalFee = rawPrice * 0.1
  finalPrice = rawPrice - rentalFee
else:
  discount = totalOrderPrice * 0.25
  discountPrice = totalOrderPrice - discount
  
  rentalFee = discountPrice * 0.1
  finalPrice = discountPrice - rentalFee

# print("{:.2f}".format(finalPrice))
print(finalPrice)