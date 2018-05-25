from DataStructures.node import Node
import random

class Minimax:

    def __init__(self,tree,utilityMap, utilityNodes):
        self.T = tree
        self.utilityMap = utilityMap

        self.utilityNodes = utilityNodes

    def isTerminal(self,state):
        if state in self.utilityNodes:
            return True
        return False

    def minimax_decision(self,state):
        depth4 = self.utilityNodes
        depth3 = self.T.getDepth3()
        depth2 = self.T.getDepth2()
        depth1 = self.T.getDepth1()
        minDepth3 = {}
        maxDepth2 = {}
        minDepth1 = {}
        tempChild = []
        min = 99999
        max =-99999
        for node in depth3:
            childList = self.T.getChildren(node)
            for child in childList:
                # print('MIN: ' + str(self.utilityMap[child]))
                if min > self.utilityMap[child]:
                    min = self.utilityMap[child]
                    # print('MIN Escogido: '+str(min))
            minDepth3[node] = min

        for node in depth2:
            childList = self.T.getChildren(node)
            for child in childList:
                if max < minDepth3[child]:
                    max = minDepth3[child]
                    # print('MAX: ' + str(max))
            maxDepth2[node] = max

        max = -99999
        min = 99999
        for node in depth1:
            childList = self.T.getChildren(node)
            for child in childList:
                if min > maxDepth2[child]:
                    min = maxDepth2[child]
                    # print('MIN: ' + str(min))
            minDepth1[node] = min

        posibleSol = []
        for node in depth1:
            if max <= minDepth1[node]:
                max = minDepth1[node]
                posibleSol.append(node)


        length = len(posibleSol)-1
        result = posibleSol[random.randint(0,length)]
        return result

    def clear(self):
        self.T = None
        self.utilityMap = None
        self.minimaxResult = None
        self.utilityNodes = None