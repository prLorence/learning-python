# always add 25 for 911
# additional minutes or text = user input minutes (or text) - 60 (or 100)
# additional minutes charge = additional minutes * 6.50
# additional texts charge = additional texts * 1
# five percent tax = raw answer * 0.05
# final answer = five percent tax + raw answer
# create a variable inside the if with additionalCharge is 0
# store the computed variable and use that inside the formula

calls = int(input("enter the number of minutes of call: "))
text = int(input("enter the number of texts: "))

planPrice = 799
offeredMinutes = 60
offeredTexts = 100
prrdFee = 25
tax = 0.05


if calls < offeredMinutes:
  minutes = offeredMinutes - calls
  additionalCallsCharge = 0
  computedCalls = minutes * 6.50
  planPrice -= computedCalls
else:
  minutes = calls - offeredMinutes
  additionalCallsCharge = minutes * 6.50
  computedCalls = additionalCallsCharge
  
additionalTexts = text - offeredTexts
additionalTextsCharge = additionalTexts * 1

rawTotal = planPrice + computedCalls + additionalTextsCharge + prrdFee
taxCharge = rawTotal * 0.05

finalTotal = rawTotal + taxCharge 

print('Call minutes: {:.1f}\nText messages: {:.1f}\nExcess minute charges: {:.2f}\nExcess SMS charges: {:.2f}\n911 fee: {:.2f}\nTax: {:.2f}\nTotal bill: {:.2f}'.format(calls, text, additionalCallsCharge, additionalTextsCharge, prrdFee, taxCharge, finalTotal))
