yourMoves = [['X', 1], ['Y', 2], ['Z', 3]]

moveCombos = [['A', 'X', 3], ['A', 'Y', 6], ['A', 'Z', 0], ['B', 'X', 0], ['B', 'Y', 3], ['B', 'Z', 6], ['C', 'X', 6], ['C', 'Y', 0], ['C', 'Z', 3]]

def GetTurns():
    with open("input.txt") as f:
        lines = f.readlines()
        turns = []
        for i in lines:
            i = i.strip('\n')
            moves = i.split(" ")
            turns.append(moves)
        return(turns)

def getYourMove(move):
    for y in yourMoves:
        if move[0] == y[0]:
            return y[1]

def getWinner(move):
    for combos in moveCombos:
        if (move[0] == combos[0]) & (move[1] == combos[1]):
            return combos[2]

def CheckMove(move):
    yourMove = getYourMove(move[1])
    winPoints = getWinner(move)
    return yourMove + winPoints

def GetResult():
    turns = GetTurns()
    total = 0
    for turn in turns:
        total += CheckMove(turn)
    print(total)

GetResult()