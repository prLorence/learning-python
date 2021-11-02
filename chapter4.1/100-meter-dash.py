# add all the inputs
# 1 minute is equal to 60 seconds
# deduct the total sum from the 1 minute equivalent
# add one to the minute counter and add the difference to the seconds counter
 
firstRunner = int(input("Enter the first runner: "))
secondRunner = int(input("Enter the second runner: "))
thirdRunner = int(input("Enter the third runner: "))

totalTime = firstRunner + secondRunner + thirdRunner

minutes = 0
second = 0

if totalTime > 60:
  totalTime -= 60
  seconds = totalTime
  minutes += 1
  print(f"{minutes}:{seconds}")
elif totalTime > 120:
  totalTime -= 120
  seconds = totalTime
  minutes += 2
  print(f"{minutes}:{seconds}")
else:
  print(f"0:{totalTime}")

