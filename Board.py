from DataStructures.tree import Tree
from Minimax import Minimax

import copy

class Board:

    def __init__(self):
        self.T = Tree()
        self.initialState = []
        self.utilityMap = {}
        self.player1 = 1
        self.player2 = 2
        self.numberOfRows = 6
        self.nextStateValue = []

    def buildBoardTree(self,state):
        self.T.insertNode(state, None)
        self.generateNodes(self.T.getRoot(), self.player2,self.numberOfRows)
        childrenDepth2 = []
        childrenDepth3 = []
        childrenDepth4 = []
        childrenDepth1 = self.T.getChildren(self.T.getRoot())
        print(len(childrenDepth1))
        for child in childrenDepth1:
            if not self.T.getChildren(child):
                self.generateNodes(child, self.player1,self.numberOfRows)

        for parent in childrenDepth1:
            for child in self.T.getChildren(parent):
                childrenDepth2.append(child)
        print(len(childrenDepth2))
        for child in childrenDepth2:
            if not self.T.getChildren(child):
                self.generateNodes(child, self.player2,self.numberOfRows)

        for parent in childrenDepth2:
            for child in self.T.getChildren(parent):
                childrenDepth3.append(child)
        print(len(childrenDepth3))
        for child in childrenDepth3:
            if not self.T.getChildren(child):
                self.generateNodes(child, self.player1,self.numberOfRows)

        for parent in childrenDepth3:
            for child in self.T.getChildren(parent):
                childrenDepth4.append(child)
        print(len(childrenDepth4))

        self.mapUtility(childrenDepth1)
        self.mapUtility(childrenDepth2)
        self.mapUtility(childrenDepth3)
        self.mapUtility(childrenDepth4)

    def generateNodes(self, state, player,count):
        if count >= 0:
            currentState = copy.deepcopy(state.getValue())
            for row in reversed(currentState):
                if row[count] == 0:
                    row[count] = player
                    break
            self.T.insertNode(copy.deepcopy(currentState), state.getValue())
            self.generateNodes(state, player, count-1)


    def getInitialState(self):
        return [[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],]

    def displayGameBoard(self):
        for row in self.T.getRoot().getValue():
            print(row)
        print('********************************************')

    def mapUtility(self, successors):
        for node in successors:
            self.utilityMap[node] = self.getUtility(node)

    def getUtility(self, node):
        utilityValue1 = self.getPlayerUtility(node,self.player1)+2
        utilityValue2 = self.getPlayerUtility(node,self.player2)
        return utilityValue1+utilityValue2

    def getPlayerUtility(self, node, player):
        string = ''
        fila = []
        columna = []
        for row in node.getValue():
            for ficha in row:
                string = string + str(ficha)
            fila.append(string)
            string = ''

        column0 = ''
        column1 = ''
        column2 = ''
        column3 = ''
        column4 = ''
        column5 = ''
        column6 = ''
        for row in node.getValue():
            column0 = column0 + str(row[0])
            column1 = column1 + str(row[1])
            column2 = column2 + str(row[2])
            column3 = column3 + str(row[3])
            column4 = column4 + str(row[4])
            column5 = column5 + str(row[5])
            column6 = column6 + str(row[6])

        columna.append(column0)
        columna.append(column1)
        columna.append(column2)
        columna.append(column3)
        columna.append(column4)
        columna.append(column5)
        columna.append(column6)

        horizontalCounter = 0
        verticalCounter = 0
        diagonalCounter = 0
        for row in fila:
            horizontalCounter = row.count(str(player)) + horizontalCounter
        for col in columna:
            verticalCounter = col.count(str(player)) + verticalCounter

        start = 0
        for count in range(6):
            i = 5
            for j in range(start,7):
                if i < 0 or (i == 5 and j == 4) or (i == 5 and j ==5) or (i == 5 and j==6): break
                if fila[i][j] == player:
                    diagonalCounter = diagonalCounter + 1
                i = i - 1
            start = start + 1

        start = 4
        for count in range(6):
            temp = start
            for j in range(7):
                if temp < 0 or (temp == 0 and j == 0) or (temp == 2 and j ==0) or (temp ==1 and j==0): break
                if fila[temp][j] == player:
                    diagonalCounter = diagonalCounter + 1
                temp = temp - 1
            start = start -1

        start = 7
        for count in range(6):
            i = 5
            for j in reversed(range(start)):
                if i < 0 or (i == 5 and j == 2) or (i == 5 and j ==1) or (i == 5 and j == 0): break
                if fila[i][j] == player:
                    diagonalCounter = diagonalCounter + 1
                i = i - 1
            start = start - 1

        start = 4
        for count in range(6):
            temp = start
            for j in reversed(range(7)):
                if temp < 0 or (temp == 2 and j == 6) or (temp == 1 and j ==6) or (temp == 0 and j == 6): break
                if fila[temp][j] == player:
                    diagonalCounter = diagonalCounter + 1
                temp = temp - 1
            start = start - 1

        return horizontalCounter + verticalCounter + diagonalCounter

    def AIply(self):
        minimax = Minimax(self.T,self.utilityMap)
        nextState = minimax.minimax_decision(self.T.getRoot())
        self.nextStateValue = nextState.getValue()


    def resetTree(self):
        self.T.clear()
        del self.initialState
        del self.utilityMap
        return self.nextStateValue
