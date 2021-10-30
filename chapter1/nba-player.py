inches = float(input("Enter the height of the player: "))
player = input("Enter the name of the player: ")

inchesToFoot = divmod(inches, 12)

print(f"Standing at {inchesToFoot[0]}\'{inchesToFoot[1]}\'\', {player}")