# two steps at recursion:
# 1. define the base case - condition to decide which step to take
# 2. recurse 

def factorial(n):
  if n <= 1:
    return n
  return n * factorial(n-1)

print(factorial(5))