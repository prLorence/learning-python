# loopVal = ask for number of people
# loop through loopVal times and ask for gender
# .toLower(gender)
# store genders inside array
# loop inside gender array

import math

loopVal = int(input("How many people?: "))
genderList = []
maleCount = 0
femaleCount = 0
femaleRatio = 0
maleRatio = 0

for i in range(loopVal):
  gender = str.lower(input("Enter your gender: "))
  genderList.append(gender)

for i in genderList:
  if i == "m":
    maleCount += 1
  else:
    femaleCount += 1

if maleCount == loopVal:
  print(f"Males: {maleCount}\nFemales: {femaleCount}\nAll males")

if femaleCount == loopVal:
  print(f"Males: {maleCount}\nFemales: {femaleCount}\nAll females")


gcd = math.gcd(maleCount, femaleCount)


if maleCount / gcd != 0:
  if femaleCount / gcd != 0:
    femaleRatio = int(femaleCount / gcd)
    maleRatio = int(maleCount / gcd)
    print(f"Males: {maleCount}\nFemales: {femaleCount}\n{maleRatio}:{femaleRatio}")


