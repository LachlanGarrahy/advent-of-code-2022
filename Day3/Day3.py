def getData():
    with open("input.txt") as f:
        lines = f.readlines()
        return(lines)

def splitData(dataEntry):
    data = []
    for i in dataEntry:
        s1 = i[:len(i)//2]
        s2 = i[len(i)//2:]
        sack = [s1, s2]
        data.append(sack)
    return(data)

def checkData(firstHalf, secondHalf):
    for i in firstHalf:
        if i in secondHalf:
            return i

def checkLetter(letter):
    if letter.isupper():
        outcome = ord(letter) - 38
    else:
        outcome = ord(letter) - 96
    return outcome


def run():
    data = getData()
    data = splitData(data)
    repeat = 0
    total = 0
    for sack in data:
        repeat = checkData(sack[0], sack[1])
        if repeat != 0:
            total += checkLetter(repeat)
    return total

print(run())