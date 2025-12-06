input = open("day6/input.txt", "r")
lines = input.readlines()
homework = []
total = 0

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

print(total)
