from DataStructures.node import Node


class Minimax:

    def __init__(self,tree,utilityMap):
        self.MIN = 0
        self.MAX = 0
        self.T = tree
        self.utilityMap = utilityMap
        self.minimaxResult = Node(None,None)
        self.utilityNodes = []

    def isTerminal(self,state):
        if not self.T.getChildren(state):
            self.utilityNodes.append(state)
            return True
        return False

    def minimax_decision(self,state):
        utilityValue = self.maxValue(state)
        self.minimaxResult = self.findSuccessorByUtilityValue(utilityValue)
        return self.minimaxResult


    def maxValue(self,state):
        if self.isTerminal(state):
            return self.utilityMap[state]

        utilityValue = -9999
        successors = self.T.getChildren(state)
        for s in successors:
            utilityValue = max(utilityValue,self.minValue(s))

        return utilityValue

    def minValue(self,state):
        if self.isTerminal(state):
            return self.utilityMap[state]
        utilityValue = 9999
        successors = self.T.getChildren(state)
        for s in successors:
            utilityValue = min(utilityValue,self.maxValue(s))
        return utilityValue

    def findSuccessorByUtilityValue(self, utilityValue):

        for node in self.utilityNodes:
            if utilityValue == self.utilityMap[node]:
                resultNode = node

        for depth in range(3):
            parentValue = resultNode.getParent()
            for child in self.T.children:
                if child.getValue() == parentValue:
                    resultNode = child

        return resultNode




