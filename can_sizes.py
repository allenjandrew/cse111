import math

print()

'''Should this be included in the main() function? I didn't include it because I see it as outside data.'''
can_data = ['#1 Picnic,6.83,10.16,$0.28','#1 Tall,7.78,11.91,$0.43','#2,8.73,11.59,$0.45','#2.5,10.32,11.91,$0.61','#3 Cylinder,10.79,17.78,$0.86','#5,13.02,14.29,$0.83','#6Z,5.40,8.89,$0.22','#8Z short,6.83,7.62,$0.26','#10,15.72,17.78,$1.53','#211,6.83,12.38,$0.34','#300,7.62,11.27,$0.38','#303,8.10,11.11,$0.42'] # Name,Radius (centimeters),Height (centimeters),Cost per Can (U.S. dollars)

def main():
    '''Variables to store data on the most efficient cans'''
    best_stor_eff = ['',0]
    best_cost_eff = ['',0]

    for entry in can_data:
        this_can = entry.split(',')
        radius = float(this_can[1])
        height = float(this_can[2])
        price = float(this_can[3].replace('$',''))

        '''Trying to reduce unecessary variables by calling all the functions together'''
        can_stor_eff = storage_efficiency(can_volume(radius,height),can_surface(radius,height))
        can_cost_eff = cost_efficiency(can_volume(radius,height),price)
        '''Print this can's efficiency values'''
        print(f'{this_can[0]}\n  Storage Efficiency: {can_stor_eff:.2f}\n  Cost Efficiency: {can_cost_eff:.0f}')

        '''Check if this can has better efficiencies than the previous best; if so, update the previous best variable'''
        if can_stor_eff > best_stor_eff[1]:
            best_stor_eff = [this_can[0],can_stor_eff]
        if can_cost_eff > best_cost_eff[1]:
            best_cost_eff = [this_can[0],can_cost_eff]

    '''Print the highest efficiency cans' data'''
    print(f'Best storage efficiency: {best_stor_eff[1]:.2f} ({best_stor_eff[0]})')
    print(f'Best cost efficiency: {best_cost_eff[1]:.0f} ({best_cost_eff[0]})')

def can_volume(radius,height):
    '''Takes the radius and height of a cylinder and returns the volume'''
    return math.pi * radius**2 * height

def can_surface(radius,height):
    '''Takes the radius and height of a cylinder and returns the surface area'''
    return 2 * math.pi * radius * (radius + height)

def storage_efficiency(volume,surface_area):
    '''Takes the volume and surface area of a cylinder (tin can) and returns the storage efficiency'''
    return volume / surface_area

def cost_efficiency(volume, price):
    '''Takes the volume and price of a tin can and returns the cost efficiency'''
    return volume / price


main()

print()