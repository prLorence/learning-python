import math

a = int(input("Give me the first length: "))
b = int(input("Give me the second length: "))

aSquared = pow(a, 2)
bSquared = pow(b, 2)



c = math.sqrt(aSquared + bSquared)

cRounded = round(c, 3)

print("The length of the diagonal is {0}.".format(cRounded))