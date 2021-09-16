#circleV2
#This version will require a user input

import (math)

input_radius = float(input("Input the radius value: "))

cir = 2 * math.pi * input_radius
area = math.pi * input_radius * input_radius

print ("Circumference = ", cir, "Area = ", area)

print(type(input_radius))