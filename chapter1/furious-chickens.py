import math

# degree * math.pi / 180

initVelocity = float(input("initVelocity "))
degrees = float(input("degrees "))
time = float(input("time "))
gravity = 9.8

degreesToRadians = degrees * (math.pi / 180)

xValue = initVelocity * math.cos(degreesToRadians) * time
yValue = initVelocity * math.sin(degreesToRadians) * time - (0.5 * gravity * time ** 2)


print(round(xValue), round(yValue))