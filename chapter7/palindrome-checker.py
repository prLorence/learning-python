# identify the base cases
# my option are: go left and right (- , +)
# first base case - return true if it is only a letter
# second base case - return true if the first letter and last letter matches
# create a function that checks if the word is a palindrome recursively
def isPalindrome(word):
    if len(word) <= 1:
        return True
    elif word[0] == word[-1]:
        return isPalindrome(word[1:-1])
    else:
        return False


def display(word):
    if isPalindrome(word):
        print(word, "is a palindrome")
    else:
        print(word, "is not a palindrome")

print(isPalindrome("dog"))
