# import math
# print()

# print(type(len(list((round(math.sqrt(abs(float(str(int(input('Please enter an integer: '))))))),)))))

# print()

# sourceFile = open('python.txt', 'w')

# print(5, 2, sep=':', end=' big unicorns\n', file=sourceFile, flush=True)
# print('hello')
# sourceFile.close()

# print()

# def is_even():
#     return math.ceil(((17**9) / 3)) - 6 % 2 == 0

# print(is_even())

# print()

# import random
# rand_list = []

# for i in range(10):
#     rand_num = random.randint(1,100)
#     rand_list.append(rand_num)

# rand_list.sort()
# print(rand_list)

print()

from datetime import datetime

if datetime.now().minute % 2 == 0:
    print('even minute')
else:
    print('odd minute')

print()