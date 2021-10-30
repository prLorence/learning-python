# stick to one comparison operator, take the higher value.

date = int(input("Enter the date number: "))
month = str.lower(input("Enter the month: "))

if month == "december" or month == "january":
  if date >= 22 or date >= 19:
    print("Your Astrological sign is : Capricorn")
elif month == "january" or month == "february":
  if date <= 20 or date >= 18:
    print("Your Astrological sign is : Aquarius")
elif month == "february" or month == "march":
  if date <= 20 or date >= 19:
    print("Your Astrological sign is : Pisces")
elif month == "march" or month == "april":
  if date <= 21 or date >= 19:
    print("Your Astrological sign is : Aries")
elif month == "april" or month == "may":
  if date <= 20:
    print("Your Astrological sign is : Taurus")
elif month == "may" or month == "june":
  if date <= 22 or date >= 19:
    print("Your Astrological sign is : Gemini")
elif month == "june" or month == "july":
  if date <= 21 or date >= 22:
    print("Your Astrological sign is : Cancer")
elif month == "july" or month == "august":
  if date <= 23 or date >= 22:
    print("Your Astrological sign is : Leo")
elif month == "august" or month == "september":
  if date <= 23 or date >= 22:
    print("Your Astrological sign is : Virgo")
elif month == "september" or month == "october":
  if date <= 23 or date >= 21:
    print("Your Astrological sign is : Libra")
elif month == "october" or month == "november":
  if date <= 23:
    print("Your Astrological sign is : Scorpio")
elif month == "november" or month == "december" and date <= 22:
    print("Your Astrological sign is : Sagittarius")
else:
  print("")
