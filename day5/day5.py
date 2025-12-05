input = open("day5/input.txt", "r")
lines = input.readlines()
validIds = []
validCount = 0
foundBreak = False

for line in lines:
    line = line.rstrip()
    if line == "":
        foundBreak = True
    else:
        if not foundBreak:
            limits = line.split('-')
            validIds.append([int(limits[0]), int(limits[1]) + 1])
        else:
            valid = False
            for idRange in validIds:
                if int(line) >= idRange[0] and int(line) <= idRange[1]:
                    valid = True
            if valid:
                validCount += 1

print(validCount)