def getData():
    with open("input.txt") as f:
        lines = f.readlines()
        return(lines)

def splitData(dataEntry):
    data = []
    i=0
    while i < len(dataEntry):
        team = dataEntry[i], dataEntry[i+1], dataEntry[i+2]
        data.append(team)
        i+=3
    return(data)

def checkData(firstSack, secondSack, thirdSack):
    for i in firstSack:
        if (i in secondSack) & (i in thirdSack):
            return i

def checkLetter(letter):
    if letter.isupper():
        outcome = ord(letter) - 38
    else:
        outcome = ord(letter) - 96
    return outcome

def run():
    data = splitData(getData())
    repeat = 0
    total = 0
    for set in data:
        repeat = checkData(set[0], set[1], set[2])
        if repeat != 0:
            total += checkLetter(repeat)
    return total

print(run())