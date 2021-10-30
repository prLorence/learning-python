# dont accept the if the value inside sqrt is negative
# prioritze solving inside the sqrt first
import math

a = int(input("enter the value of a: "))
b = int(input("enter the value of b: "))
c = int(input("enter the value of c: "))

insideSquareRoot = (b ** 2) - (4 * (a * c))

if insideSquareRoot < 0:
  print("There are no solutions")
else:
  quadratic_1 = float(-b + (math.sqrt(insideSquareRoot)))/(2 * a)
  quadratic_2 = float(-b - (math.sqrt(insideSquareRoot)))/(2 * a)
  print(f"There are two solutions , namely {quadratic_1} and {quadratic_2}")
 