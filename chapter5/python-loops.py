num = int(input("Enter a number: "))


# while loop in python
total = 0

while num != 0:
    total += num
    num = int(input("Enter a number: "))
print ("The total is", total)

# for loop in python
word = input("Please enter any word:")

for letter in word:
  print(letter)

# this is the equivalent of three part for loop in python (i think)
for i in range(10):
  print(i)