yourMoves = [['X', 0], ['Y', 3], ['Z', 6]]

moveCombos = [['A', 'X', 3], ['A', 'Y', 1], ['A', 'Z', 2], ['B', 'X', 1], ['B', 'Y', 2], ['B', 'Z', 3], ['C', 'X', 2], ['C', 'Y', 3], ['C', 'Z', 1]]

def GetTurns():
    with open("input.txt") as f:
        lines = f.readlines()
        turns = []
        for i in lines:
            i = i.strip('\n')
            moves = i.split(" ")
            turns.append(moves)
        return(turns)

def getRoundStatus(move):
    for y in yourMoves:
        if move[0] == y[0]:
            return y[1]

def getPlayerMove(move):
    for combos in moveCombos:
        if (move[0] == combos[0]) & (move[1] == combos[1]):
            return combos[2]

def CheckMove(move):
    roundStatus = getRoundStatus(move[1])
    playerMove = getPlayerMove(move)
    return roundStatus + playerMove

def GetResult():
    turns = GetTurns()
    total = 0
    for turn in turns:
        total += CheckMove(turn)
    print(total)

GetResult()