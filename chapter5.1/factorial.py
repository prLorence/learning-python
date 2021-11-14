factorial = int(input("Enter a number to be factored: "))
counter = 1
answer = 1

while factorial >= counter:
  if factorial < 2:
    print(1)
    break
  answer = counter * answer
  counter += 1

print(answer)

