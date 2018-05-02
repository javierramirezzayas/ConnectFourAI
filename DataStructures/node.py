
class Node:

    def __init__(self, p, v, tag):
        self.parent = p
        self.value = v
        self.tag = tag

    def getParent(self):
        return self.parent

    def getValue(self):
        return self.value

    def getTag(self):
        return self.tag

    def setTag(self, tag):
        self.tag = tag

    def setParent(self, p):
        self.parent = p

    def setValue(self, v):
        self.value = v