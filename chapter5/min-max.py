# ask for 10 numbers
i = 1
numList = []

while i < 10:
  val = int(input("Enter a number: "))
  numList.append(val)
  if len(numList) == 10:
    print(numList)
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
  if i % 3 == 1:
    divisible += 1
  

print("The largest number is: ", largest)
print("The smallest number is: ", smallest)
print("The number of numbers divisible by 3 is: ", divisible)
