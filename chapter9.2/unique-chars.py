# create a function that returns the number of unique characters in a string using dictionaries
def unique_chars_in_a_string(string):
  unique_char_dict = {}
  for char in string:
    if char not in unique_char_dict:
      unique_char_dict[char] = 1
    else:
      unique_char_dict[char] += 1
  return f"The entered string contains", len(unique_char_dict), "unique character(s)."


print(unique_chars_in_a_string("Hello, World!"))