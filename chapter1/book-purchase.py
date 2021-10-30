#solution here
bookSize = float(input("Please enter any amount of books to be shipped: "))

bookPrice = 24.95
discount = 0.40
shipping_1 = 3.0 #first copy
shipping_2 = 0.75 # additional shipping costs per copy

rawPrice = float(bookSize * bookPrice)
discount = float(rawPrice * discount)
discountedPrice = float(rawPrice - discount)
firstCopy = float(discountedPrice + 3) # Additional $3 for first copy
remainingCopies = float((bookSize - 1) * shipping_2) # multiplies remaining copies with additional shipping costs
finalPrice = firstCopy + remainingCopies

# print(Decimal(finalPrice) - Decimal(0.001))

print(finalPrice - 0.0000000000001)