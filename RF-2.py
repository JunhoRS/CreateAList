# Create a recursive function that determines if a number is prime or not.
    

def prime_number(number, n=2):
    if n >= number:
        return True
    elif number % n != 0:
        return prime_number(number, n + 1)
    else:
        return False

# Verify that the code runs
result = prime_number(4)
print (result) 