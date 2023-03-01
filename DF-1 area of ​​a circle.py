# 1-Create a function that calculates the area of ​​a circle given its radius..

def calculate_circle_area(radio):
    area = 3.14159 * (radio ** 2)
    return area

# Verify that the code runs

area = calculate_circle_area(19)
print(area)