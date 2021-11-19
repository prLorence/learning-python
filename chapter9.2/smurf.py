# create a function the counts all of the characters inside a string and returns a dictionary
def charCount(string):
  char_dict = {}
  for char in string:
    if char not in char_dict:
      char_dict[char] = 1
    else:
      char_dict[char] += 1
  return char_dict

# create a function that removes spaces of a string
def removePunctuation(value):
  value = value.replace(" ", "")
  value = value.replace("\n", "")
  return value

# create a function that compares the two strings and decide whether the two strings have the same characters
def compareStrings(string1, string2):
  string1 = removePunctuation(string1)
  string2 = removePunctuation(string2)
  if charCount(string1) == charCount(string2):
    return True
  else:
    return False



