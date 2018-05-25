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
        self.nextStateValue = []
        self.utilityNodes = []
        self.root = []

    def buildBoardTree(self,state):
        self.root = self.T.insertNode(state, None,'0')
        depth0 = []

        depth0.append(self.root)
        self.createBranches(depth0, self.player2, '1')
        depth1 = self.T.getDepth1()
        self.createBranches(depth1, self.player1, '2')
        depth2 = self.T.getDepth2()
        self.createBranches(depth2, self.player2, '3')
        depth3 = self.T.getDepth3()
        self.createBranches(depth3, self.player1, '4')
        depth4 = self.T.getDepth4()

        self.mapUtility(depth4)
        self.utilityNodes = depth4


    def createBranches(self, depthLevel, player, tag):
        for node in depthLevel:
            self.generateNodes(node, player, 6, tag)

    def generateNodes(self, state, player,count,tag):
        stateIsNew = False
        if count >= 0:
            currentState = copy.deepcopy(state.getValue())
            for row in reversed(currentState):
                if row[count] == 0:
                    row[count] = player
                    stateIsNew = True
                    break
            if stateIsNew:
                self.T.insertNode(copy.deepcopy(currentState), state.getValue(), tag)
            self.generateNodes(state, player, count-1,tag)


    def getInitialState(self):
        return [[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],]

    def displayGameBoard(self):
        for row in self.root.getValue():
            print(row)

    def mapUtility(self, successors):
        for node in successors:
            self.utilityMap[node] = self.getUtility(node)

    def getUtility(self, node):
        AIthree = 0
        AItwo = 0
        Playerthree = 0
        Playertwo = 0
        Playerhorizontal = self.getHorizontalCount(node,self.player1)
        Playervertical = self.getVerticalCount(node,self.player1)

        AIhorizontal = self.getHorizontalCount(node, self.player2)
        AIvertical = self.getVerticalCount(node, self.player2)

        if AIhorizontal == 2:
            AIthree = AIthree +1

        if AIvertical == 2:
            AIthree = AIthree + 1

        if Playerhorizontal == 2:
            Playerthree = Playerthree +1

        if Playervertical == 2:
            Playerthree = Playerthree + 1

        if AIhorizontal == 1:
            AItwo = AItwo +1

        if AIvertical == 1:
            AItwo = AItwo + 1

        if Playerhorizontal == 1:
            Playertwo = Playertwo +1

        if Playervertical == 1:
            Playertwo = Playertwo + 1

        AIthree = AIthree*1000
        AItwo = AItwo*10
        Playerthree = Playerthree*1000
        Playertwo = Playertwo*10

        score = AIthree + AItwo - Playerthree - Playertwo
        return score

    def getHorizontalCount(self, node, player):
        horizontalCounter = 0
        value = node.getValue()
        for row in value:
            horizontalCounter = horizontalCounter + self.checker(0,player,row)
        return horizontalCounter

    def getVerticalCount(self, node, player):
        verticalCounter = 0
        column0 = []
        column1 = []
        column2 = []
        column3 = []
        column4 = []
        column5 = []
        column6 = []

        for row in node.getValue():
            column0.append(row[0])
            column1.append(row[1])
            column2.append(row[2])
            column3.append(row[3])
            column4.append(row[4])
            column5.append(row[5])
            column6.append(row[6])
        verticalCounter = self.checkerC(0,player,column0) + verticalCounter
        verticalCounter = self.checkerC(0, player, column1) + verticalCounter
        verticalCounter = self.checkerC(0, player, column2) + verticalCounter
        verticalCounter = self.checkerC(0, player, column3) + verticalCounter
        verticalCounter = self.checkerC(0, player, column4) + verticalCounter
        verticalCounter = self.checkerC(0, player, column5) + verticalCounter
        verticalCounter = self.checkerC(0, player, column6) + verticalCounter
        return verticalCounter

    def checker(self,counter,player,value):
        prev = player
        isConsecutive = False
        for ficha in value:
            if player == ficha and isConsecutive:
                counter = counter + 1
            elif player == ficha:
                isConsecutive = True
            elif ficha != 0 and prev == player:
                counter = 0
                isConsecutive = False
            elif ficha == 0 and prev != 0:
                isConsecutive = False
            prev = ficha
        return counter

    def checkerC(self,counter,player,value):
        prev = player
        isConsecutive = False


        for ficha in value:
            if player == ficha and isConsecutive:
                counter = counter + 1
            elif player == ficha:
                isConsecutive = True
            elif ficha != 0 and prev == player:
                counter = 0
                isConsecutive = False
            elif ficha == 0 and prev != 0:
                isConsecutive = False
            prev = ficha
        return counter

    def AIply(self):
        minimax = Minimax(self.T,self.utilityMap,self.utilityNodes)
        nextState = minimax.minimax_decision(self.root)
        self.nextStateValue = nextState.getValue()
        minimax.clear()
        print('*************************************************')
        print('*       The Computer Has Made Its Move!         *')
        print('*************************************************')
        return self.nextStateValue