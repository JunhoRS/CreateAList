# Write a recursive function that calculates the factorial of a number.


def factorial(F):
    if F == 1:
        return 1 
    else:
        return F * factorial(F - 1)


# Verify that the code runs
result = factorial(7)
print (result) 
