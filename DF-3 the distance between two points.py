# 3- Create a function that calculates the distance between two points on a Cartesian plane.

import math

def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Verify that the code runs
distance = calculate_distance(1, 2, 4, 6)
print(distance)
