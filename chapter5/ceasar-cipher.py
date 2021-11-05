# loop through the word and convert it to ascii
# add the ascii value of the key from the user input
# convert the ascii value back to a characters
# leave non-letters as is

word = input("Enter a word: ")
shiftVal = int(input("Enter your desired shift value: "))

for i in range(len(word)):
    asciiVal = ord(word[i])
    if asciiVal >= 97 and asciiVal <= 122:
        asciiVal += shiftVal
        if asciiVal > 122:
            asciiVal -= 26
        print(chr(asciiVal), end="")
    elif asciiVal >= 65 and asciiVal <= 90:
        asciiVal += shiftVal
        if asciiVal > 90:
            asciiVal -= 26
        print(chr(asciiVal), end="")
    else:
        print(word[i], end="")