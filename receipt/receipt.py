import csv
import datetime
import sys

print()

def main():
    PRO_NUM_IND = 0
    QUANT_IND = 1
    NAME_IND = 1
    PRICE_IND = 2

    try: products_dict = read_dictionary('receipt/products.csv',PRO_NUM_IND)
    except PermissionError:
        print('You don\'t have permission to view that file. Loser.\n')
        sys.exit()
    except FileNotFoundError:
        print('That file doesn\'t exist. Just like your dad\n')
        sys.exit()
    # print(products_dict)

    print('\nWelcome to Ardy\'s!')
    print('\nRequested Items:\n')

    with open('receipt/request.csv') as cust_order:
        reader = csv.reader(cust_order)
        next(reader)
        total_cost = 0
        total_items = 0

        for line in reader:
            try:
                product = products_dict[line[PRO_NUM_IND]]
                num_items = int(line[QUANT_IND])
                product_cost = num_items * float(product[PRICE_IND])
                print(f'{product[NAME_IND].capitalize()}: {line[QUANT_IND]} @ ${product[PRICE_IND]} ea ----- ${product_cost:.2f}')
                total_cost += product_cost
                total_items += num_items
            except KeyError as keyE:
                print(f'You\'ve got a problem. {keyE} is not a valid product number. We\'ve removed it from your order.')

        print(f'\n{total_items} total items')
        print(f'Subtotal ----- ${total_cost:.2f}')
        sales_tax = total_cost * .06
        total_cost += sales_tax
        print(f'Sales tax ----- ${sales_tax:.2f}')
        print(f'Total cost ----- ${total_cost:.2f}')

        print('\nThank you for shopping at Ardy\'s! See you soon!')
        print(datetime.datetime.now().strftime('%c'))
    


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    with open(filename) as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for line in reader:
            if len(line) != 0:
                key = line[key_column_index]
                dictionary[key] = line
    return dictionary

if __name__ == '__main__':
    main()

print()