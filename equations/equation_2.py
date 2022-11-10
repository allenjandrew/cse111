from math import sqrt
print()

def x_function(a, b, c):
    if (4 * a * c) <= (b**2):
        return (0 - b + sqrt(b ** 2 - (4 * a * c))) / (2 * a)
    else:
        return complex((0 - b) / (2 * a), sqrt(abs((b ** 2) - (4 * a * c))) / (2 * a))

print(f'{x_function(22, 66, 9):.3f}')
print(f'{x_function(9, 1, 4):.3f}')

print()
