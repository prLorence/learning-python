# use divmod and add [1] with 5

year = int(input("Please enter a year: ")) 

# if (year - 2000) % 12 == 0 or (year - 1900) % 12 == 0 or (year - 1800) % 12 == 0:
#   print("Dragon")
# elif (year - 2000) % 12 == 1 or (year - 1900) % 12 == 1 or (year - 1800) % 12 == 1:
#   print("Snake")   
# elif (year - 2000) % 12 == 2 or (year - 1900) % 12 == 2 or (year - 1800) % 12 == 2:
#   print("Horse")
# elif (year - 2000) % 12 == 3 or (year - 1900) % 12 == 3 or (year - 1800) % 12 == 3:
#   print("Sheep")
# elif (year - 2000) % 12 == 4 or (year - 1900) % 12 == 4 or (year - 1800) % 12 == 4:
#   print("Monkey")
# elif (year - 2000) % 12 == 5 or (year - 1900) % 12 == 5 or (year - 1800) % 12 == 5:
#   print("Rooster")
# elif (year - 2000) % 12 == 6 or (year - 1900) % 12 == 6 or (year - 1800) % 12 == 6:
#   print("Dog")
# elif (year - 2000) % 12 == 7 or (year - 1900) % 12 == 7 or (year - 1800) % 12 == 7:
#   print("Boar")
# elif (year - 2000) % 12 == 8 or (year - 1900) % 12 == 8 or (year - 1800) % 12 == 8:
#   print("Rat")
# elif (year - 2000) % 12 == 9 or (year - 1900) % 12 == 9 or (year - 1800) % 12 == 9:
#   print("Ox")
# elif (year - 2000) % 12 == 10 or (year - 1900) % 12 == 10 or (year - 1800) % 12 == 10:
#   print("Tiger")
# else:
#   print("Hare")


if year % 12 == 0:
  print("Dragon")
elif year % 12 == 1:
  print("Snake")   
elif year % 12 == 2:
  print("Horse")
elif year % 12 == 3:
  print("Sheep")
elif year % 12 == 4:
  print("Monkey")
elif year % 12 == 5:
  print("Rooster")
elif year % 12 == 6:
  print("Dog")
elif year % 12 == 7:
  print("Boar")
elif year % 12 == 8:
  print("Rat")
elif year % 12 == 9:
  print("Ox")
elif year % 12 == 10:
  print("Tiger")
else:
  print("Hare")