input = open("day1/input.txt", "r")
lines = input.readlines()
start = 50
counter = 0

for line in lines:
    line = line.rstrip()
    dir = line[0]
    dist = int(line[1:])
    if dir == "L":
        if start - dist < 0:
            start = ((start - dist) % 100)
        else:
            start -= dist
    elif dir == "R":
        if start + dist > 99:
            start = ((start + dist) % 100)
        else:
            start += dist
    if start == 0:
        counter += 1

print(counter)