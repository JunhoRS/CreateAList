# Write a recursive function that calculates the nth term of the Fibonacci series.

def fibonacci(n):
   if n <= 2:
      return n - 1
   else:
      return fibonacci(n - 1) + fibonacci(n - 2)


# Verify that the code runs
n = 2
print(fibonacci(n))
