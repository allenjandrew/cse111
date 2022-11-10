import csv

print()

def main():
    dict_file = read_dict('students/students.csv')
    print(dict_file)

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