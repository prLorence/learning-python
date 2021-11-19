def factorGenerator(n):
  factor_list = []
  # return all of the factors of n
  for i in range(1, n + 1):
    if n % i == 0:
      factor_list.append(i)
  factor_list.pop()
  return factor_list



def isPerfect(n):
  factor_list = factorGenerator(n)
  sum_of_factors = sum(factor_list)
  if sum_of_factors == n:
    return True
  return False


print(isPerfect(50))