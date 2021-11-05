# ask for 10 numbers
i = 1
numList = []

while i < 10:
  val = int(input("Enter a number: "))
  numList.append(val)
  if len(numList) == 10:
    break
i += 1

largest = 0
smallest = numList[0]
divisible = 0

# find the largest and smallest number inside array with for loop
for i in numList:
  if i > largest:
    largest = i
  # find the smallest number inside the array
if i < smallest:
    smallest = i
if i % 3 == 0:
    divisible += 1
  

print(f"Highest: {largest}\nLowest: {smallest}\n{divisible} numbers divisible by 3", )


