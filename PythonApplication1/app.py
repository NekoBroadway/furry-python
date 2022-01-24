#Exc 4 - Write a Python program which accepts the radius of a circle from the user and compute the area

from math import pi


radius = input("Podaj średnicę koła: ")
area = pow(float(radius), 2) * pi

print(f"Pole koła o średnicy {radius} równa się {area}")