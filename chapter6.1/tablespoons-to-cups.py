# create a function that takes two parameters
# one is for the number and one for the units to be converted
# the function should return the converted value in string format
def reduce_measure(num, unit):
  if unit == "tablespoons":
    num = divmod(num, 16)
    return f"{num[0]} cups, {num[1]} tablespoons"
  elif unit == "cups":
    return str(num) + " cups"
  elif unit == "teaspoons":
    num = divmod(num, 48)
    return f"{num[0]} cups, {num[1]} teaspoons"
  else:
    return str(num) + " " + unit





print(reduce_measure(59, "tablespoons"))
print(reduce_measure(2, "cups"))
print(reduce_measure(97, "teaspoons"))
