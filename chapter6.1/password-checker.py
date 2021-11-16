def checkPassword(password):
  if len(password) < 8:
    return False
  if not any(char.isdigit() for char in password):
    return False
  if not any(char.isupper() for char in password):
    return False
  if not any(char.islower() for char in password):
    return False
  return True
  
def display(password):
  if checkPassword(password):
    return "Password is valid"
  else:
    return "Password is invalid"

print(display('hello'))
print(display('aahdd4Dshsd'))
print(display('CHDS4all'))
