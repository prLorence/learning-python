principal = int(input("principal ples: "))
rate = float(input("rate ples: ")) / 100
years = int(input("years ples: "))

interest = principal * ((1 + rate) ** years)

print("{:.2f}".format(interest))