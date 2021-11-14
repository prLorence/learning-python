def multiple(x):
  printVal = ""
  for i in range(1, x + 1):
    printVal += "x"
  return printVal

def print_x(x):
  for i in range(1, x + 1):
    print(multiple(i))

multiple(5)
print_x(5)