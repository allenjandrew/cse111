import random

print()

def main():
    numbers = [16.2, 75.1, 52.3]
    print(numbers)
    append_random_numbers(numbers)
    print(numbers)
    append_random_numbers(numbers, quantity=3)
    print(numbers)

def append_random_numbers(numbers_list, quantity=1):
    for _ in range(quantity):
        new_number = random.uniform(0,100)
        rounded_number = round(new_number, 1)
        numbers_list.append(rounded_number)

if __name__ == '__main__':
    main()

print()