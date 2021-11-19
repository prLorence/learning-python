# ((2, 1), (0, 2)) != ('(2 ,1i)', '*', '(0 ,2i)', '=', '(-2 ,4i)')
# ('(2, 1i)', '*', '(0, 2i)', '=', '(-2, 4i)') != ('(2 ,1i)', ' * ', '(0 ,2i)', '=', '(-2 ,4i)')

def multiply_complex(c1,c2):
  # c1 = (a, b), c2 = (c, d)
  
  first_product = str(((c1[0] * c2[0]) - (c1[1] * c2[1])))
  second_product = str(((c1[0] * c2[1]) - (c1[1] * c2[0]))) + "i"
  return f"({first_product}, {second_product})"

def display_complex(c):
  t = multiply_complex(c)
  return t

def display(num1,num2):

  num1_first_str = str(num1[0])
  num1_second_str = str(num1[1]) + "i"
  num2_first_str = num2[0]
  num2_second_str = str(num2[1]) + "i"
  num1_str = f"({num1_first_str} ,{num1_second_str})"
  num2_str = f"({num2_first_str} ,{num2_second_str})"
  return f"{num1_str}", "*", f"{num2_str}", "=", f"{multiply_complex(num1,num2)}"

print(multiply_complex((2,1), (0,2)))
print(display((2,1), (0,2)))


