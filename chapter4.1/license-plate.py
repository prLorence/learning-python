# license format : AAA - nnn

# reading a string of characters from the user. 
# the string is a license plate number 

licensePlate = input("Enter your license plate number: ")

if licensePlate == "":
    print("The plate is not valid")
elif licensePlate[0].isalpha() and licensePlate[1].isalpha() and licensePlate[2].isdigit() and licensePlate[3].isdigit() and licensePlate[4].isdigit() and licensePlate[5].isdigit():
    print("The plate is a valid older style plate.")
elif licensePlate[0].isdigit() and licensePlate[1].isdigit() and licensePlate[2].isdigit() and licensePlate[3].isdigit() and licensePlate[4].isalpha() and licensePlate[5].isalpha() and licensePlate[6].isalpha():
    print("The plate is a valid newer style plate.")
else:
    print("The plate is not valid")


