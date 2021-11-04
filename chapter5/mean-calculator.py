numVal = int(input("Enter a value: "))
numList = []

numList.append(numVal)

if numVal == 0:
  print("No entries")

while numVal != 0:
  numVal = int(input("Enter a value: "))
  numList.append(numVal)
  if numVal == 0:
    print(int(sum(numList) / len(numList)))
    break
  