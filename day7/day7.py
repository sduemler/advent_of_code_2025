input = open("day7/input.txt", "r")
lines = input.readlines()
mani = []
tachyonCount = 0

for line in lines:
    line = line.rstrip()
    man = list(line)
    mani.append(man)

for x in range(len(mani)):
    print(mani[x])
    for y in range(len(mani[x])):
        if mani[x][y] == 'S' or mani[x][y] == '|':
            if x < len(mani) - 1:
                if mani[x+1][y] == '.':
                    mani[x+1][y] = '|'
                elif mani[x+1][y] == '^':
                    split = False
                    if y != 0:
                        if mani[x+1][y-1] == '.':
                            mani[x+1][y-1] = '|'
                            split = True
                    if y < len(mani[x]) - 1:
                        if mani[x+1][y+1] == '.':
                            mani[x+1][y+1] = '|'
                            split = True
                    if split:
                        tachyonCount += 1

print(tachyonCount)