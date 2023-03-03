# 2- Write a function that takes a list of numbers and returns the largest number in the list.

def largest_number(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

# Verify that the code runs
numbers = [10, 5, 20, 3, 15]
largest = largest_number(numbers)
print(largest)