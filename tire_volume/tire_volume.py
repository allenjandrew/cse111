import math

print()

print('Welcome! Let\'s find the volume in your tires.\n')

print('Enter the tire size for your vehicle. You can find this number in two places:')
print('1. Sidewall of your tire.\n2. Inside frame of the driver side door.\n')

print('You can type in the full tire size here, or press ENTER to type in each value separately. Please do not include spaces.')
tire_size = input('Tire size (eg. 205/60R15): ')

tire_width = ''
aspect_ratio = ''
wheel_di = ''

if tire_size == '': # if the user hits Enter without putting in the tire size
    tire_width = input('Enter the width of the tire in mm (eg. 205): ')
    aspect_ratio = input('Enter the aspect ratio of the tire (eg. 60): ')
    wheel_di = input('Enter the diameter of the wheel in inches (eg. 15): ')
else:
    tire_width = ''
    aspect_ratio = ''
    wheel_di = ''
    destination = 1
    for character in tire_size: # to separate the three numbers from the string tire_size
        if not character.isnumeric():
            destination += 1
        elif destination == 1:
            tire_width += character
        elif destination == 2:
            aspect_ratio += character
        elif destination == 3:
            wheel_di += character
        if destination == 4: # to stop the loop before looking at load and speed ratings 
            break

w = int(tire_width)
a = int(aspect_ratio)
d = int(wheel_di)

v = (math.pi * (w ** 2) * a * (w * a + 2540 * d)) / 10000000000

# print(tire_width, aspect_ratio, wheel_di)

print(f'\nThe approximate volume is {v:.2f} liters')

print()

from datetime import datetime

volumes_file = open('volumes.txt', 'a')
volumes_file.write(f'{datetime.now().date()}, {w}mm, {a}, {d}in, {v:.2f}L\n')
volumes_file.close()