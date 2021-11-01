# may and october (deluxe)  = 100 * number of nights
# may and october (premium) = 85 * number of nights 
# july and september (deluxe) = 112.50 * number of nights
# july and september (premium) = 90.58 * number of nights
# june and august (deluxe) = 125.66 * number of nights
# june and august (premium) = 100.50 * number of nights
# get deluxe and premium price for
# after nested ifs, print the prices


month = str.lower(input("Please enter a month: "))
nights = int(input("Please enter the number of nights: "))

if month == "may" or month == "october":
  if nights > 7 and nights < 14:
    moDeluxeRaw = 100 * nights 
    discount = moDeluxeRaw * 0.05
    moDeluxe = moDeluxeRaw - discount
  elif nights > 14:
    moDeluxeRaw = 100 * nights
    discount = moDeluxeRaw * 0.30
    moDeluxe = moDeluxeRaw - discount
    moPremiumRaw = 85 * nights
    discount = moPremiumRaw * 0.10
    moPremium = moPremiumRaw - discount
  else:
    moDeluxe = 100 * nights
    moPremium = 85 * nights
  print("Deluxe: {:.2f} dollars\nPremium: {:.2f} dollars".format(moDeluxe, moPremium))
elif month == "july" or month == "september":
  if nights > 14:
    jsDeluxeRaw = 112.50 * nights
    discount = jsDeluxeRaw * 0.20
    jsDeluxe = jsDeluxeRaw - discount
  elif nights > 14:
    jsPremiumRaw = 90.58 * nights
    discount = jsPremiumRaw * 0.10
    jsPremium = jsPremiumRaw - discount
  else:
    jsDeluxe = 112.50 * nights
    jsDeluxe = 90.58 * nights
  print("Deluxe: {:.2f} dollars\nPremium: {:.2f} dollars".format(jsDeluxe, jsPremium))
elif month == "june" or month == "august":  
  if nights > 14:
    jaPremiumRaw = 100.50 * nights
    discount = jaPremiumRaw * 0.10
    jsPremium = jaPremiumRaw - discount
  else:
    jaDeluxe = 125.66 * nights
    jaPremium = 100.50 * nights
  print("Deluxe: {:.2f} dollars\nPremium: {:.2f} dollars".format(jaDeluxe, jaPremium))
