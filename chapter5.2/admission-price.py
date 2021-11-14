age = input("Enter your age: ")
age_list = []
age_list.append(age)
cost = 0
# 2 <= == free admission
# >= 3 and <= 12 == $14.00
# >= 65 == $18.00
# > 12 and < 65 == $12.00 


while age != "end":
  age = input("Enter your age: ")
  age_list.append(age)

  if age == "end":
    age_list.pop()
    # print(age_list)
    for i in range(len(age_list)):
      if float(age_list[i]) < 3:
        cost
      elif float(age_list[i]) >= 3 and int(age_list[i]) <= 12:
        cost += 14.00
      elif float(age_list[i]) >= 65:
        cost += 18.00
      else:
        cost += 23.00
    break
  
print(cost)