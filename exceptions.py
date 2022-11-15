print()

truth = True

while truth:
    try:
        x = int(input('Enter a number between 0 and 5: '))
        if x > 5 or x < 0:
            raise Exception()
    except ValueError as value_e:
        print('Try making it an integer this time, buddy.')
    except:
        print('That number isn\'t in the correct range. Try again.')
    else: truth = False
    finally: print(':P')