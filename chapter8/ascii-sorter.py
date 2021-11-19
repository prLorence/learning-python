# sort the given string according to the ascii value of each character
str = input("Enter your")
sorted_str = "".join(sorted(str, key=lambda x: ord(x)))
print(sort_char(str))
    