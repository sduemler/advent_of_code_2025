input = open("day2/input.txt", "r")
lines = input.readlines()

line = lines[0].rstrip().split(",")

invalids = 0
moreInvalids = 0

for x in line:
    inputRange = x.split("-")
    start = int(inputRange[0])
    end = int(inputRange[1])
    for y in range(start, end+1):
        id = str(y)
        if len(id) % 2 == 0:
            firstId = id[0:int(len(id)/2)]
            secondId = id[int(len(id)/2):len(id)]
            if firstId == secondId:
                invalids += y
    for y in range(start, end+1):
        id = str(y)
        foundInvalid = False
        for z in range(len(id) // 2):
            if len(id) % len(id[:z+1]) == 0:
                multiples = len(id) / len(id[:z+1])
                if id.count(id[:z+1]) == multiples and not foundInvalid:
                    moreInvalids += y
                    foundInvalid = True



print(invalids)
print(moreInvalids)