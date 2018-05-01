from DataStructures.node import Node


class Minimax:

    def __init__(self,tree):
        self.MIN = 0
        self.MAX = 0
        self.T = tree


    # def minima_decision(self,state):

    def maxValue(self,state):
        if isTerminal(state)
        utilityValue = -9999
        successors = self.T.getChildren(state)
        for s in successors:
            utilityValue = max(utilityValue,self.minValue(state))

    def minValue(self,state):
        utilityValue = -9999


