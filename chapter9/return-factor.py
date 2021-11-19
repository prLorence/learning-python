def return_factor(n):
    factor_list = []
    # return all of the factors of n
    for i in range(1, n + 1):
        if n % i == 0:
            factor_list.append(i)
    return factor_list
print(return_factor(100))