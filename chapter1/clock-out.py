currentTime = 14.00 
alarmTime = 535.00
difference = alarmTime - currentTime
hours = int(round((difference / 60) + 12)) # converts 12 hour format to 24 hour format 

print("%.2f"%hours)