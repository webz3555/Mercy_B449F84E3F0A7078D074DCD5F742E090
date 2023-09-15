# Recursive function to find factorial of a number
def factorial(n):

  # base case: if `n` is 0 or 1
  if n < 1:
    return 1

  # use the recurrence relation
  return n * factorial(n - 1)


if __name__ == '__main__':

  n = 5
  print(f'The Factorial of {n} is', factorial(n))
