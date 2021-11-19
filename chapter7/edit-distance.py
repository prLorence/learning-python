# create a function that checks the measure of the similarity of the two words recursively
def editDistance(word1, word2):
    if len(word1) == 0:
        return len(word2)
    elif len(word2) == 0:
        return len(word1)
    elif word1[0] == word2[0]:
        return editDistance(word1[1:], word2[1:])
    else:
        return 1 + min(editDistance(word1[1:], word2), editDistance(word1, word2[1:]), editDistance(word1[1:], word2[1:]))

def display(word1, word2):
   return f"The edit distance between kitten and sitting is {editDistance(word1,word2)}" 

print(display("cake", "bake"))