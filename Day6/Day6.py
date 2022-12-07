def day6(distinctChar):
    charList = []
    with open("input.txt") as f:
        line = f.readlines()[0]
        for char in range(len(line)):
            charList.append(line[char])
            if(len(charList) != len(set(charList))):
                charList.pop(0)
                continue
            if(len(charList) == distinctChar):
                print(char+1)
                break

day6(4)
day6(14)