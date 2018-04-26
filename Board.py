from DataStructures.tree import Tree

import copy

class Board:

    def __init__(self):
        self.T = Tree()
        self.initialState = []

    def generateSuccessors(self, state):
        global initialState
        initialState = state
        self.T.insertNode(state,None)
        for i in range(7):
            currentState = copy.deepcopy(state)
            for row in reversed(currentState):
                if row[i] == 0:
                    row[i] = 2
                    break
            self.T.insertNode(copy.deepcopy(currentState),state)

    def getInitialState(self):
        return [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]

    def displayGameTree(self):
        self.T.display()