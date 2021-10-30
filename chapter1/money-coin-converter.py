money = float(input('Please any amount of money: '))


# Takes all dollars
dollarsInMoney = divmod(money, 1.0)
dollars = round(int(float(dollarsInMoney[0])))
dollarsChange = float(dollarsInMoney[1])

# Takes all quarters 
quartersInDollars  = divmod(dollarsChange, 0.25)
quarters = round(int(float(quartersInDollars[0])))
quartersChange = float(quartersInDollars[1])

# Takes all dimes
dimesInquarters = divmod(quartersChange, 0.1)
dimes = round(int(float(dimesInquarters[0])))
dimesChange = float(dimesInquarters[1])

# Takes all nickels 
nickelsInDimes = divmod(dimesChange, 0.05)
nickels = round(int(float(nickelsInDimes[0])))
nickelsChange = float(nickelsInDimes[1])

# Takes all pennies
penniesInDimes = divmod(nickelsChange, 0.01)
pennies = round(int(float(penniesInDimes[0])))

# print(f"{money} consists of: \nDollars: {dollars}\nQuarters: {quarters}\nDimes: {dimes}\nNickels: {nickels}\nPennies: {pennies}")

print(f'{money} consists of:\nDollars: {dollars}\nQuarters: {quarters}\nDimes: {dimes}\nNickels: {nickels}\nPennies: {pennies}')