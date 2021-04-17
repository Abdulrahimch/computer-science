def sum_digits(n):
  result = 0
  if n < 0:
    raise ValueError("Inputs 0 or greater only!")
  if n == 0:
    return n
  result += n % 10
  n = n // 10
  return result + sum_digits(n)

# test cases
print(sum_digits(12) == 3)
print(sum_digits(552) == 12)
print(sum_digits(123456789) == 45)