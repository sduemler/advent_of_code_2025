input = open("day3/input.txt", "r")
lines = input.readlines()
totalJolts = 0

for line in lines:
    line = line.rstrip()
    firstBattery = 0
    secondBattery = 0
    for x in range(len(line)-1):
        if x == 0:
            firstBattery = int(line[0])
            secondBattery = int(line[1])
        else:
            if int(line[x]) > firstBattery:
                firstBattery = int(line[x])
                secondBattery = int(line[x+1])
            elif int(line[x+1]) > secondBattery:
                secondBattery = int(line[x+1])
    totalJolts += int(str(firstBattery) + str(secondBattery))

print(totalJolts)
    