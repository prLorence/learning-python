# create a program that reads x and y value
# first x times second y
# first y times second x
# two arrays, one for x and one for y
# 

xArray = []
yArray = []
xValue = input("Please enter an x-value: ")

xArray.append(int(xValue))

while xValue != "stop":
  yValue = input("Please enter a y-value: ")
  xValue = input("Please enter an x-value: ")
  if yValue == "stop" and xValue == "stop":
    print("do some stuff")
    break


# yArray.append(int(yValue))
# xArray.append(int(xValue))

print(xArray, yArray)
