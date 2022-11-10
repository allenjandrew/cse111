from copy import deepcopy
print()

lego_line = [8, 12, 47, 36, 19, 84, 1, 99]
saved_line = deepcopy(lego_line)
sorted = False

print(lego_line)

while not sorted:
    sorted = True
    for i in range(0, len(lego_line) - 1):
        if lego_line[i] < lego_line[i+1]:
            lego_line[i], lego_line[i+1] = lego_line[i+1], lego_line[i]
            sorted = False

print(lego_line)
print(saved_line)

print()

new_line = []

for stack in saved_line:
    if not new_line:
        new_line.append(stack)
    else:
        for i in range(0, len(new_line)):
            if stack > new_line[i]:
                new_line.insert(i, stack)
                break
            else:
                new_line.append(stack)
                break

print(new_line)
print(saved_line)

print()