# write a function that returns the approximate value of pi using greogory leibnitz series

def gregoryLeibnitz(num):
    pi = 0
    for i in range(num):
        pi += ((-1)**i)/(2*i+1)
    return pi*4


print(gregoryLeibnitz(20))