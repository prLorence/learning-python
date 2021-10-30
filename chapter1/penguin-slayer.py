import math

x1 = int(input("enter the first value of x: "))
y1 = int(input("enter the first value of y: "))
x2 = int(input("enter the second value of x: "))
y2 = int(input("enter the second value of y: "))

xSquared = (x2 - x1) ** 2
ySquared = (y2 - y1) ** 2

distance = float(math.sqrt(xSquared + ySquared))

print("{:.2f}".format(distance))