def gcd(n, m):
    if n == 0:
        return m
    return gcd(m % n, n)

def reduce(num, den):
    g = gcd(num, den)
    return num // g, den // g

def display(num, den):
   answer = reduce(num, den)
   return f"{num}/{den} can be reduced to {answer[0]}/{answer[1]}."

print(display(4, 100))

