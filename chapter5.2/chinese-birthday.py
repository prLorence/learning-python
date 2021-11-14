# loop through the range(years)
# if even - receive previous money given + 10 dollars 
# if odd - toys += 1
# toys_sum = toys_price * toys
# total = money + toys_sum
# toys are sold at toy_price
# money - washing machine price


years = int(input("How old: "))
washing_machine_price = int(input("How much is the washing machine worth: "))
toy_price = int(input("How much is the toy worth: "))

money = 0
money_counter = 0
toys = 0

for i in range(1, years + 1):
    # if i is even money_counter goes up
    if i % 2 == 0:
        money_counter += 1
    else:
        toys += 1
    
for j in range(1, money_counter + 1):
    money += (10 * j) - 1

toys_sum = float(toy_price * toys)
total = float(money + toys_sum) 
extra = float(total - washing_machine_price)

if extra > 0:
    print("Yes! you still have {:.2f} left".format(extra))
else:
    extra = abs(extra)
    print("No! you still need {:.2f}".format(extra))










