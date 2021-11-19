# calculate the greatest common divisor of two numbers using euclid's algorithm
def calculate(a, b):
    if b == 0:
        return a
    return calculate(b, a % b)
print(calculate(60, 35))