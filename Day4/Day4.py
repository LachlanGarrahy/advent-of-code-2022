def getData():
    with open("input.txt") as f:
        lines = f.readlines()
        return(lines)

def splitData(dataEntry):
    data = []
    for i in dataEntry:
        i = i.strip("\n")
        ranges = i.split(",")
        areas = []
        for range in ranges:
            a = range.split("-")
            areas.append(a)
        team = [areas[0], areas[1]]
        data.append(team)
    return(data)

def checkData(firstMember, secondMember):
    range1 = range(int(firstMember[0]), int(firstMember[1])+1)
    range2 = range(int(secondMember[0]), int(secondMember[1])+1)

    if(len(range1) == 0 and range1.start in range2):
        return True
    if(len(range2) == 0 and range2.start in range1):
        return True

    if(range1.start in range2 and range1[-1] in range2 or range2.start in range1 and range2[-1] in range1):
        return True

def run():
    data = getData()
    split = splitData(data)
    total = 0
    for assignments in split:
        if(checkData(assignments[0], assignments[1])):
            total+=1
    print(total)

run()