def getData():
    with open("input.txt") as f:
        lines = f.readlines()
        data = []
        input = []
        moves = False
        for line in lines:
            if(line == "\n"):
                moves = True
                continue
            if (not moves):
                data.append(line)
                continue
            input.append(line)
        return(data, input)

def splitData(data):
    grid = [[],[],[],[],[],[],[],[],[]]
    character = 0
    for line in data:
        character = 0
        if(line[0] == " "):
            return grid
        while(character<36):
            if(line[character+1] == " "):
                character+=4
                continue
            grid[character//4].append(line[character+1])
            character+=4

def splitInput(input):
    import re
    moves = []
    for line in input:
        line = line.replace("move ", "").replace("from ", "").replace("to ", "").replace("\n", "")
        move = re.split("\s", line)
        result = [eval(i) for i in move]
        moves.append(result)
    return moves

def processData(stacks, move):
    while move[0] > 0:
        box = stacks[move[1]-1][0]
        stacks[move[1]-1].pop(0)
        stacks[move[2]-1].insert(0, box)
        move[0]-=1
    return stacks


def run():
    data, input = getData()
    stacks = splitData(data)
    moves = splitInput(input)
    for move in moves:
        processData(stacks, move)
    for stack in stacks:
        print(stack)
run()