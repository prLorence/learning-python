# start at M
# end at N
# power at P times
# if the counter reaches p, start at new line

start = int(input("Enter the starting point: "))
end = int(input("Enter the ending point: "))
power = int(input("Enter the power value: "))

answer = 1

for i in range(start, end + 1):
  for k in range(2, power):
    answer = str(i ** k)
    print(answer, end = ", ")
    # if k reaches power, start new line
    if k == power - 1:
      fourth_item = i ** (k + 1)
      print(fourth_item)








   
      
      
      