# ill take an input
# then divide that input from 1111 to 9999 each of its digits

input_number = int(input("Please enter a number: "))
list = []
answer_list = []
temp = []
single_digit = 0

for i in range(1111, 2222):
    list.append(str(i))
    for j in range(len(list)): # this is the list of numbers in string format
      for k in range(len(list[j])): # acccessing the single digit
        single_digit = int(list[j][k]) # turns the single digit string into int
        if input_number % single_digit == 0: # checks if that single digit has no remainder when divided from the input
          print("divisible")
          answer_list.append(str(single_digit))
          if single_digit == 0:
            continue
          # join the array of strings when the list reaches length of 3



print(answer_list)   
# if it is divisible, convert it into a string then append it to some list 
# and when that list reaches the length of 3, join them. 