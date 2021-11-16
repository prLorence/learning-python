def capitalize(sentence):
    for i in range(len(sentence)):
      # capitalize only the small letter i 
      if i == 0 or sentence[i] == "i" and sentence[i-1] and sentence[i + 1] == " ":
        sentence = sentence[:i] + sentence[i].upper() + sentence[i+1:]
        
    return sentence

test_sentence = "what time do i have to be there? what’s the address?"

print(capitalize(test_sentence))