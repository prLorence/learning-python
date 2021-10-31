# A = 8.5 , 9.0, 9.5, 10.0
# B = 8.0
# C = 6.5, 7.0
# D = 6 
# F = 


grade = float(input("Please enter the grade: "))

if grade == 8.5 or grade == 9.0 or grade == 9.5 or grade == 10 and grade % 0.5 == 0:
  print("Grade A")
elif grade == 8.0 and grade % 0.5 == 0:
  print("Grade B")
elif grade == 6.5 or grade == 7.0 and grade % 0.5 == 0:
  print("Grade C")
elif grade == 6 and grade % 0.5 == 0:
  print("Grade D")
elif grade < 6 and grade % 0.5 == 0:
  print("Grade F")
else:
  print("Grades should be rounded to the nearest half point.")
  