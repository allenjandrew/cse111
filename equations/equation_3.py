import math
print()

def compute_area(r):
    return math.pi * r**2

radius = float(input('Please enter the radius: '))

print(f'The area of the circle is {compute_area(radius):.3f}')

print()