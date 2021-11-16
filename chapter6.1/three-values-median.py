def median(a, b, c):
    if a < b:
        if b < c:
            return b
        elif a < c:
            return c
        else:
            return a
    elif a < c:
        return a
    elif b < c:
        return c
    else:
        return b

def alternate_median(a, b, c):
  return median(a, b, c) + 2

def print_ans(a,b,c):
  median_val = median(a,b,c)
  alternate_median_val = alternate_median(a,b,c)
  return f"The median value is {median_val} and the value for the alternate median function is {alternate_median_val}"

print(print_ans(1,5,7))
print(print_ans(41,5,7))
print(print_ans(50,15,7))