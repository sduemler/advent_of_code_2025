input = open("day5/input.txt", "r")
lines = input.readlines()
validIds = []
validCount = 0
moreValidCount = 0
foundBreak = False

for line in lines:
    line = line.rstrip()
    if line == "":
        foundBreak = True
    else:
        if not foundBreak:
            limits = line.split('-')
            validIds.append([int(limits[0]), int(limits[1])])
        else:
            valid = False
            for idRange in validIds:
                if int(line) >= idRange[0] and int(line) <= idRange[1]:
                    valid = True
            if valid:
                validCount += 1

swapped = True

"""
two for loops:
    one for looping through the original list
        keeps getting reset back to the first until they are all good
    one for checking that first for loop with all the
    other ranges in the same list

    checks if low end is in range
        if high end in range then delete entry
        if high end above then modify entry to have new high entry and remove entry
    elif high end in range:
        if low end below then set new low end and remove entry

    if any changes, change swapped to true

    if swap is true, set x back to 0
"""

while(swapped):
    swapped = False
    for x in range(len(validIds)):
        swapped = False
        for y in range(len(validIds)):
            itself = False
            origin = validIds[x]
            check = validIds[y]
            if origin[0] == check[0] and origin[1] == check[1]:
                if itself:
                    validIds.remove(origin)
                    swapped = True
                    break
                else:
                    itself = True
                    continue
            elif origin[0] >= check[0] and origin[0] <= check[1]:
                # left limit is within
                if origin[1] <= check[1]:
                    # upper limit within, remove
                    validIds.remove(origin)
                    swapped = True
                    break
                elif origin[1] > check[1]:
                    # upper limit above, grow and remove
                    validIds[y][1] = origin[1]
                    validIds.remove(origin)
                    swapped = True
                    break
            elif origin[1] <= check[1] and origin[1] >= check[0]:
                if origin[0] < check[0]:
                    validIds[y][0] = origin[0]
                    validIds.remove(origin)
                    swapped = True
                    break
            else:
                continue
        if swapped:
            break
        else:
            continue

finalValids = []
# remove any duplicates
for id in validIds:
    if id not in finalValids:
        finalValids.append(id)

for id in finalValids:
    moreValidCount += id[1] - id[0] + 1
        

print(validIds)
print(validCount)
print(moreValidCount)

#tried:
# 1726069340674834
# 363611670203150
# 343329651880509