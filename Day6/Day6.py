def day6(distinctChar):
    charList = []
    counter = 0
    for l in open('input.txt'):
        for char in l:
            counter += 1
            charList.append(char)
            if(len(charList) != len(set(charList))):
                charList.pop(0)
                continue
            if(len(charList) == distinctChar):
                break
    print(counter)

day6(4)
day6(14)