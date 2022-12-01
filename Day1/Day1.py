
def GetCalories():
    with open("input.txt") as f:
        lines = f.readlines()
        calories = []
        currentCalories = 0
        for i in lines:
            if i == "\n":
                calories.append(currentCalories)
                currentCalories = 0
            else:
                currentCalories += int(i)
        return(calories)
        
def SortList(calories):
    calories.sort(reverse=True)
    return calories

def addTopThree(calories):
    return calories[0] + calories[1] + calories[2]

def printCounts(calories, top3):
    print(max(calories))
    print(top3)

calories = GetCalories()
sortedCalories = SortList(calories)
totalTop3 = addTopThree(sortedCalories)
printCounts(calories, totalTop3)