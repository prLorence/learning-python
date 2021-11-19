# create a function that takes a string as an argument and separate them recursively without converting them in to a list
# remove the blank chars if there's any



def tokenList(s):
  tokens = [c for c in s if c != " "]
  return f"Tokens are {tokens}"


print(tokens())
