from DataStructures.node import Node


class Minimax:

    def __init__(self,tree,utilityMap, utilityNodes):
        self.T = tree
        self.utilityMap = utilityMap
        self.minimaxResult = Node(Node,Node,'')
        self.utilityNodes = utilityNodes
        self.tempUtilityValue = 0

    def isTerminal(self,state):
        if state in self.utilityNodes:
            return True
        return False

    def minimax_decision(self,state):
        self.maxValue(state)
        self.findMinimaxResultNode()
        return self.minimaxResult


    def maxValue(self,state):
        if self.isTerminal(state):
            return self.utilityMap[state]

        utilityValue = -9999
        successors = self.T.getChildren(state)
        for s in successors:
            utilityValue = max(utilityValue,self.minValue(s))
            if utilityValue != self.tempUtilityValue:
                self.tempUtilityValue = utilityValue
                self.minimaxResult = s


        return utilityValue

    def minValue(self,state):
        if self.isTerminal(state):
            return self.utilityMap[state]
        utilityValue = 9999
        successors = self.T.getChildren(state)
        for s in successors:
            utilityValue = min(utilityValue,self.maxValue(s))
            if utilityValue != self.tempUtilityValue:
                self.tempUtilityValue = utilityValue
                self.minimaxResult = s
        return utilityValue

    def clear(self):
        self.T = None
        self.utilityMap = None
        self.minimaxResult = None
        self.utilityNodes = None

    def findMinimaxResultNode(self):

        for node in self.T.getDepth3():
            if self.minimaxResult.getParent() == node.getValue():
                self.minimaxResult = node
                break

        for node in self.T.getDepth2():
            if self.minimaxResult.getParent() == node.getValue():
                self.minimaxResult = node
                break

        for node in self.T.getDepth1():
            if self.minimaxResult.getParent() == node.getValue():
                self.minimaxResult = node
                break








