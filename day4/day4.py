input = open("day4/input.txt", "r")
lines = input.readlines()
validRolls = 0

rolls = []
for line in lines:
    line = line.rstrip()
    roll = []
    for x in line:
        roll.append(x)
    rolls.append(roll)

for x in range(len(rolls)):
    roll = rolls[x]
    for y in range(len(roll)):
        if roll[y] == '@':
            adj = 0
            if x > 0:
                #check the above row
                if y > 0:
                    if rolls[x-1][y-1] == '@':
                        adj += 1
                if rolls[x-1][y] == '@':
                    adj += 1
                if y < len(roll)-1:
                    if rolls[x-1][y+1] == '@':
                        adj += 1
            if x < len(rolls)-1:
                #check the below row
                if y > 0:
                    if rolls[x+1][y-1] == '@':
                        adj += 1
                if rolls[x+1][y] == '@':
                    adj += 1
                if y < len(roll)-1:
                    if rolls[x+1][y+1] == '@':
                        adj += 1
            if y > 0:
                #check left
                if roll[y-1] == '@':
                    adj += 1
            if y < len(roll)-1:
                #check right
                if roll[y+1] == '@':
                    adj += 1
            if adj < 4:
                validRolls += 1

print(validRolls)