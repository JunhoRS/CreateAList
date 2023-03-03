# From a String create a list and modify one of the elements of the list and convert it back to String.

string = "Program"


list_of_Program = list(string)

list_of_Program[0] = 'L'

back_to_string = ''.join(list_of_Program)

# Verify that the code runs
print(back_to_string)
