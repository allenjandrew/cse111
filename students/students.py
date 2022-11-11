import csv

print()

def main():
    dict_file = read_dict('students/students.csv')
    print(dict_file)
    user_inumber = input('\nPlease enter an I-Number: ').replace('-','')
    # Check that the input I-Number is valid.
    if len(user_inumber) < 9: print('Invalid I-Number: too few digits')
    elif len(user_inumber) > 9: print('Invalid I-Number: too many digits')
    elif not user_inumber.isdigit(): print('Invalid I-Number')
    # Find and print the corresponding student
    elif user_inumber in dict_file.keys(): print(*dict_file[user_inumber])
    else: print('No such student')

def read_dict(filename,key_column_index=0):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    with open(filename, 'rt') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for line in reader:
            # for key, value in line:
            #     dictionary[key] = value
            if len(line) != 0:
                key = line.pop(key_column_index)
                dictionary[key] = line
    return dictionary

if __name__ == '__main__':
    main()

print()