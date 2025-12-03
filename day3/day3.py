input = open("day3/input.txt", "r")
lines = input.readlines()
totalJolts = 0
totalBigJolts = 0

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

    batteries = line
    checkBatteries = batteries
    selectedBatteries = [0]*12
    start = 0
    for x in range(12):
        end = len(batteries) - 11 + x
        swapped = False
        selectedBatteries[x] = int(batteries[start])
        start += 1
        if start < end:
            checkBatteries = batteries[start:end]
            checks = 0
            initial = start
            for y in checkBatteries:
                checks += 1
                if int(y) > selectedBatteries[x]:
                    start = initial
                    selectedBatteries[x] = int(y)
                    start += checks
                                
    selectedBatteries = ''.join(list(map(str, selectedBatteries)))
    totalBigJolts += int(selectedBatteries)       
        



print(totalJolts)

print(totalBigJolts)
    