word = str.lower(input("Enter a word: "))
counter = 0

for vowel in "aeiou":
  if vowel in word:
    counter += 1

if counter == 1:
  print(f"There is only one different vowel in the string.")
else:
  print(f"There is only {counter} different vowel in the string.")
  
