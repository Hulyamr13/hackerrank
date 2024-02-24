import random


class Board:
    def __init__(self):
        self.currentPosition = 1
        self.ladders = []
        self.snakes = []

    def LoadLadders(self, ladders):
        self.ladders = ladders
        self.ladderPoints = [int(start) for start, end in self.ladders]

    def LoadSnakes(self, snakes):
        self.snakes = snakes
        self.snakePoints = [int(start) for start, end in self.snakes]

    def Move(self, number):
        self.currentPosition = int(self.currentPosition)
        if self.currentPosition + number > 100:
            pass
        else:
            self.currentPosition += number
            self.TriggerLadderAndSnakes()

    def IsCompleted(self):
        return self.currentPosition == 100

    def TriggerLadderAndSnakes(self):
        if int(self.currentPosition) in self.ladderPoints:
            newPosition = [end for start, end in self.ladders if int(start) == self.currentPosition]
            self.currentPosition = newPosition[0]
        elif int(self.currentPosition) in self.snakePoints:
            newPosition = [end for start, end in self.snakes if int(start) == self.currentPosition]
            self.currentPosition = newPosition[0]


class Die:
    def __init__(self, dieProbabilities):
        self.probabilityTable = dieProbabilities

    def Roll(self):
        randCounter = random.random()
        for dieVal, probability in self.probabilityTable.items():
            if randCounter <= probability:
                return int(dieVal)
            else:
                randCounter -= probability
        return 6


def GetNumberOfRolls(board, die):
    board.currentPosition = 1
    numRolls = 0
    while not board.IsCompleted():
        moveForwardNum = die.Roll()
        numRolls += 1
        board.Move(moveForwardNum)
    return numRolls


def GetAverageNumberOfRolls(board, die, totalTries):
    sumOfRolls = 0
    for game in range(0, totalTries):
        sumOfRolls += GetNumberOfRolls(board, die)
    return int(sumOfRolls / totalTries)


totalTestCases = input()
for testCase in range(0, int(totalTestCases)):
    probabilityList = [float(probability) for probability in input().split(',')]
    dieProbabilities = {dieVal: probabilityList[dieVal - 1] for dieVal in range(1, 7)}
    numLadders, numSnakes = input().split(',')
    ladderPositions = [tuple(pair.split(',')) for pair in input().split(' ')]
    snakePositions = [tuple(pair.split(',')) for pair in input().split(' ')]
    newBoard = Board()
    newBoard.LoadLadders(ladderPositions)
    newBoard.LoadSnakes(snakePositions)
    newDie = Die(dieProbabilities)
    numRolls = GetAverageNumberOfRolls(newBoard, newDie, 5000)
    print(numRolls)