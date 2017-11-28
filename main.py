import tensorflow
import numpy as np
import checkers

#Generate data
def generateData(numberSimulations):
    gameStates = []
    finalResult = []
    startingMove = []
    for x in range(0, numberSimulations):
        [rasmus, winCondition, A] = checkers.generateGames()
        startingMove.append(A)
        gameStates.append(rasmus)
        finalResult.append(winCondition)
    return [gameStates, finalResult, startingMove]

[gameStates, finalResult, startingMove] = generateData(1)

X = startingMove
y = np.array(finalResult)

def sigmoid(z):
    return 1/(1+np.exp(-z))

weightMatrix = np.random.randn(9,9)
weightMatrix2 = np.random.randn(3,9)

def forward(weights_first_layer, weights_second_layer):
    #Z = np.dot(weightMatrix, np.transpose(X))
    Z = np.dot(weights_first_layer, np.transpose(X))
    A = sigmoid(Z)
    output = np.dot(weights_second_layer, A)
    output = sigmoid(output)
    return output

def costFunction(weights, X):
    
    return
Z = forward(weightMatrix, weightMatrix2)

print Z
print X
print y
