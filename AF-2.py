# Create a new list from another by using a lambda function to filter the elements of the original list.

first_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

second_list = list(filter(lambda x: x % 4 == 1, first_list))


# Verify that the code runs
print (second_list)
