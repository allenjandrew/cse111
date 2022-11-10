print()

def main():
    num_rects = int(input('How many rectangles do you have? ')) # Get number of rectangles
    tot_area = 0
    for i in range(num_rects): # Loop the amount of times as rectangles
        # For each rectangle, get length and width from the user
        length = float(input('Enter the length: '))
        width = float(input('Enter the width: '))
        # Send it to the get_rect() function to compute area
        area = get_rect(length,width)
        print_but_its_a_new_function(f'Area: {area}')
        # Send it to the new_total() function to find new total area
        tot_area = new_total(tot_area, area)
    # After looping, display total
    print_but_its_a_new_function(f'Total area: {tot_area}')

def get_rect(length, width): # Get area from length and width
    return length * width

def new_total(running_total, new_value): # Get total from previous total and a new value
    return running_total + new_value

def print_but_its_a_new_function(string): # Just fake it
    print(string)

main()

print()