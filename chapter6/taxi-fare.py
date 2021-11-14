# take in n numbers of kilometers 
# default value is 5 kilometers
# +0.25 for every 140


def taxi(distance = 5):
  fare = 4.00
  extra_fare = 0
  if distance == 5:
    fare = "4.00"
    return fare
  else:
    extra_fare = round((distance / 140) * 0.25, 2)
    return str(fare + extra_fare)

print(taxi(5))