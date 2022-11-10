print()

def main():
    provinces_list = read_list('provinces/provinces.txt')
    print(provinces_list)
    for index_to_remove in ['first', 'last']:
        remove_index(provinces_list,index_to_remove)
    replace_instances(provinces_list,'AB','Alberta')
    num_alberta = provinces_list.count('Alberta')
    print(f'There are {num_alberta} instances of province Alberta in modified list')

def read_list(filename):
    text_list = []
    with open(filename) as text_file:
        for line in text_file:
            clean_line = line.strip()
            text_list.append(clean_line)
    return text_list

def remove_index(list,index_to_pop):
    if type(index_to_pop) == int:
        list.pop(index_to_pop)
    elif index_to_pop == 'first':
        list.pop(0)
    elif index_to_pop == 'last':
        list.pop()

def replace_instances(list,old_value,new_value):
    for i in range(len(list)):
        if list[i] == old_value: list[i] = new_value

if __name__ == '__main__':
    main()

print()