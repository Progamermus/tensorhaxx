import numpy as np
import random

startState = [[0,0,0],[0,0,0],[0,0,0]]

def makeRandomMove(gameState, turn):
    A = np.matrix(gameState)
    B = np.asarray(A).ravel()
    playableSquares = np.where(B == 0)[0]

    if(turn == 1):
        possible = len(playableSquares)-1
        move = random.randint(0,possible)
        index = playableSquares[move]
        B[index] = 1
        turn = 2
        return [B, turn]

    if(turn == 2):
        possible = len(playableSquares)-1
        move = random.randint(0,possible)
        index = playableSquares[move]
        B[index] = -1
        turn = 1
        return [B, turn]

def checkWin(gameState):
    rowSum = np.sum(gameState, axis=0)
    colSum = np.sum(gameState, axis=1)
    numberNonZeros = np.count_nonzero(gameState)

    if(3 in rowSum or 3 in colSum or np.trace(gameState) == 3 or np.trace(gameState[::-1]) == 3):
        return [1,0,0]
    if(-3 in rowSum or -3 in colSum or np.trace(gameState) == -3 or np.trace(gameState[::-1]) == -3):
        return [0,1,0]
    if(numberNonZeros == 9):
        return [0,0,1]
    else:
        return [0,0,0]

def generateGames():
    bigArray = [np.matrix(startState)]
    keepPlaying = [0,0,0]
    turn = 1

    for x in range(0,10):
        winCondition = checkWin(bigArray[x])
        if (np.sum(winCondition) > 0):
            A = np.array(bigArray[1]).flatten()
            break;
        [B, turn] = makeRandomMove(bigArray[x], turn)
        C = np.matrix(B.reshape(3,3))
        bigArray.append(C)
    return [bigArray, winCondition, A]

[rasmus, winCondition, A] = generateGames()
