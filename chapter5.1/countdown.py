count = int(input("Enter the start count-down: "))


for i in range(count, -1, -1):
  if i == 0:
    print("Blast off!")
    break
  print(i)
  
  