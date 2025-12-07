input = open("day6/input.txt", "r")
lines = input.readlines()
homework = []
total = 0
grandTotal = 0

for line in lines:
    line = line.rstrip().split(' ')
    line = [x for x in line if x]
    homework.append(line)

for x in range(len(homework[0])):
    added = 0
    multed = 1
    for y in range(len(homework)):
        if y == len(homework) - 1:
            if homework[y][x] == '+':
                total += added
            else:
                total += multed
        else:
            added += int(homework[y][x])
            multed *= int(homework[y][x])

# print(total)


inputs = []
for line in lines:
    letters = []
    for letter in line:
        if letter == '\n':
            continue
        else:
            letters.append(letter)
    inputs.append(letters)

while(" " in inputs[len(inputs)-1]):
    for x in inputs[len(inputs)-1]:
        if x == ' ':
            inputs[len(inputs)-1].remove(x)

modifiers = inputs[len(inputs)-1]
inputs.pop()

sepInputs = []
for x in range(len(inputs[0])):
    sep = []
    for y in range(len(inputs)):
        sep.append(inputs[y][x])
    sepInputs.append(''.join(sep))

modd = 0
inputs = []
inputTotal = 0
for x in sepInputs:
    if str.isspace(x):
        modd += 1
        grandTotal += inputTotal
        inputTotal = 0
    else:
        if modifiers[modd] == '+':
            inputTotal += int(x.strip())
        else:
            if inputTotal == 0:
                inputTotal += 1
            inputTotal *= int(x.strip())
grandTotal += inputTotal

print(grandTotal)
        
