
class Node:

    def __init__(self, p, v):
        self.parent = p
        self.value = v

    def getParent(self):
        return self.parent()

    def getValue(self):
        return self.value

    def setParent(self, p):
        self.parent = p

    def setValue(self, v):
        self.value = v