from DataStructures.node import Node


class Tree:

    def __init__(self):
        self.root = []
        self.children =[]
        self.numChildren = 0
        self.depth1 = []
        self.depth2 = []
        self.depth3 = []
        self.depth4 = []

    def insertNode(self, value, parent, tag):
        node = Node(parent, value, tag)
        if parent is not None:
            self.children.append(node)
            self.numChildren = self.numChildren + 1
        else:
            self.root = node

        if tag == '1':
            self.depth1.append(node)
        elif tag =='2':
            self.depth2.append(node)
        elif tag =='3':
            self.depth3.append(node)
        elif tag =='4':
            self.depth4.append(node)
        return node

    def getRoot(self):
        return self.root

    def getDepth1(self):
        return self.depth1

    def getDepth2(self):
        return self.depth2

    def getDepth3(self):
        return self.depth3

    def getDepth4(self):
        return self.depth4

    def getChildren(self, parentNode):
        tag = parentNode.getTag()
        selectedChild = []
        if tag == '0':
            childList = self.getDepth1()
        elif tag == '1':
            childList = self.getDepth2()
        elif tag == '2':
            childList = self.getDepth3()
        elif tag == '3':
            childList = self.getDepth4()

        for c in childList:
            if c.getParent() == parentNode.getValue():
                selectedChild.append(c)
        return selectedChild




    def children(self):
        return self.children()

    def getNumberOfChildren(self):
        return self.numChildren