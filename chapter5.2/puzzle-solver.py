# A, B, C, and D are all different digits.
# A is the first digit, B is the second digit, C is the third digit, and D is the fourth digit.
# The number DCBA is equal to 4 times the number ABCD.
# Find that unique number combination.


for a in range(1, 10):
  for b in range(10):
    for c in range(10):
      for d in range(10):
        if a != b and a != c and a != d and b != c and b != d and c != d:
          if a * 4 == b * 3 + c * 2 + d:
            print(d, c, b, a)
