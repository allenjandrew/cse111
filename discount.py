from datetime import datetime

print()

# subtotal = float(input('What is your subtotal? '))
price = 1
quantity = 1
subtotal = 0

print('Enter the price and quantity of the items on your order. Enter 0 to finish.\n')
while price != 0:
    price = float(input('Item price: $'))
    if price == 0:
        break
    quantity = float(input('Item quantity: '))
    if quantity == 0:
        break
    subtotal += (price * quantity)
    print()

print()

if datetime.now().weekday() in [1, 2]:
    if subtotal >= 50:
        print(f'Your discount: ${(subtotal * .1):.2f}')
        subtotal *= .9
    print(f'Add items worth ${(50 - subtotal):.2f} to your purchase to receive a 10% discount!')

print()

print(f'Your sales tax (6%): ${(subtotal * .06):.2f}')
subtotal *= 1.06

print()

print(f'Your total: ${subtotal:.2f}')

print()