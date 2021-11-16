# use the factorial function to calculate the  


def calculate(number, digits):
  if number <= 1 or digits <= 1:
    return number
  answer = factorial(number) / (factorial(digits) * factorial(number - digits)) 

  return f"1 in {round(answer)}"

def factorial(number):
  if number <= 1:
    return number
  return number * factorial(number - 1)

print(calculate(61,7))
