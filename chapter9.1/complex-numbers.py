# create a function that takes two tuple paramaters and add them together with complex numbers
# Addition of two complex numbers a + bi and c + di is defined as (a + c) + (b + d)i

def add_complex_numbers(a, b):
  # a = (x, y), b = (w, z)
  # (x + w) + (y + z)i
  a0_str = str(a[0]) 
  b0_str = str(b[0])  
  a1_str = str(a[1]) + "i"
  b1_str = str(b[1]) + "i"

  if a[1] == 1:
    a1_str = "i"
  if b[1] == 1:
    b1_str = "i"
  if a0_str == "0":
    a0_str = ""
  if b0_str == "0":
    b0_str = ""
    second_sum = f"{b1_str}"
    
  first_sum = f"{a0_str}+{a1_str}"

 # return (f"(\'({first_sum})\', \'+\', \'({second_sum})\')\'")
  return (f"({first_sum})", "+", f"({second_sum})")

print(add_complex_numbers((2, 1), (0, 2))) 
print(add_complex_numbers((5, 4), (0, 2))) 

# ('(2 + i)', '+', '(2i)') != ('(2+i)', '+', '(2i)')