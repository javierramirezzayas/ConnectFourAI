from DataStructures.node import Node

import copy

initialState =     [[0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0]]


class Board:

    def generateSuccessors(self, state):


        successors = {}

        for i in range(7):
            currentState = copy.deepcopy(state)
            for row in reversed(currentState):
                if row[i] == 0:
                    row[i] = 2
                    break
            successors[i] = copy.deepcopy(currentState)

        for z in successors:
            print("Successor state " + str(z) + '\n')
            for row in successors.get(z):
                print(str(row) + "\n")

    def getInitialState(self):
        global initialState
        return initialState