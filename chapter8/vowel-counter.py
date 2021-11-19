def vowel_counter(string):
  # count each vowel in the string and return the count of each vowel
  # vowels are aeiouAEIOU
  # count the number of vowels in the string
  # a = number of a's in the string
  # e = number of e's in the string
  # i = number of i's in the string
  # o = number of o's in the string
  # u = number of u's in the string
  # A = number of A's in the string
  # E = number of E's in the string
  # I = number of I's in the string
  # O = number of O's in the string
  # U = number of U's in the string
  # return those vowel counts

  # initialize the vowel counts
  a = 0
  e = 0
  i = 0
  o = 0
  u = 0
  # check the number of vowels in the string
  for char in string:
    if char == 'a' or char == 'A':
      a += 1
    elif char == 'e' or char == 'E':
      e += 1
    elif char == 'i' or char == 'I':
      i += 1
    elif char == 'o' or char == 'O':
      o += 1
    elif char == 'u' or char == 'U':
      u += 1
  # return the vowel counts
  return f"Counts: a={a}, e={e}, i={i}, o={o}, u={u}"

print(vowel_counter("yellowispikachu"))