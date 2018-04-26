from DataStructures.node import Node


class Tree:

    def __init__(self):
        self.root = []
        self.children =[]
        self.numChildren = 0

    def insertNode(self, value, parent=None):
        node = Node(parent,value)
        if parent is not None:
            self.children.append(node)
            self.numChildren = self.numChildren + 1
        else:
            self.root = node
        return node

    def getRoot(self):
        return self.root

    def display(self):
        print('Parent Node:\n')
        for row in self.root.getValue():
            print(row)
            print('\n')
        for n in self.children:
            print('Child Node:\n')
            for row in n.getValue():
                print(row)
                print('\n')