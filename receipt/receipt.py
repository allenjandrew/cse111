import csv

print()

def main():
    PRO_NUM_IND = 0
    QUANT_IND = 1
    NAME_IND = 1
    PRICE_IND = 2

    products_dict = read_dictionary('receipt/products.csv',PRO_NUM_IND)
    print(products_dict)

    print('\nRequested Items:')
    with open('receipt/request.csv') as cust_order:
        reader = csv.reader(cust_order)
        next(reader)
        for line in reader:
            product = products_dict[line[PRO_NUM_IND]]
            print(f'{line[QUANT_IND]} of item {product[NAME_IND]} @ ${product[PRICE_IND]} ea for total of ${int(line[QUANT_IND]) * float(product[PRICE_IND]):.2f}')

    


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