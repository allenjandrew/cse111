import math

print()

inventory = int(input('Enter the number of manufactured items in inventory: '))
per_box = int(input('Enter the number of items to pack in each box: '))

print()

print(f'For {inventory} items, packing {per_box} to a box, you will need {math.ceil(inventory/per_box)} boxes.')

print()