# create a function that takes two parameters then returns the number of duplicate letters in the two strings
# only compare the letters that are the same in both strings

def checkDuplicate(string_1, string_2):
    # create a dictionary to store the letters
    letters = {}
    # loop through the first string
    for letter in string_1:
        # if the letter is not in the dictionary, add it and set the value to 1
        if letter not in letters:
            letters[letter] = 1
        # if the letter is in the dictionary, add 1 to the value
        # else:
        #     letters[letter] += 1
    # loop through the second string
    for letter in string_2:
        # if the letter is not in the dictionary, add it and set the value to 1
        if letter not in letters:
            letters[letter] = 1
        # if the letter is in the dictionary, add 1 to the value
        else:
            letters[letter] += 1
    # create a variable to store the number of duplicate letters
    return check(letters)

# create a function that checks the duplicated letters from the dictionary
def check(letters):
    # create a variable to store the number of duplicate letters
    duplicated_letters = 0
    # loop through the dictionary
    for letter in letters:
        # if the value is greater than 1, add 1 to the duplicated_letters variable
        if letters[letter] > 1:
            duplicated_letters += 1
    # return the number of duplicated letters
    return f"The words have {duplicated_letters} characters in common"

print(checkDuplicate('happy', 'head'))
print(checkDuplicate('happend', 'head'))

