import math

input = open("day1/input.txt", "r")
lines = input.readlines()
start = 50
counter = 0
passCounter = 0

for line in lines:
    line = line.rstrip()
    dir = line[0]
    dist = int(line[1:])
    if dir == "L":
        if start - dist < 0:
            if start == 0:
                passCounter -= 1
            while start - dist < 0:
                passCounter += 1
                dist -= 100
        start -= dist
    elif dir == "R":
        if start + dist > 99:
            while start + dist > 99:
                passCounter += 1
                dist -= 100
        start += dist
        if start == 0:
            passCounter -= 1
    if start == 0:
        counter += 1
    print("start " + str(start))
    print("passCounter " + str(passCounter))

print(counter)

print(counter + passCounter)
