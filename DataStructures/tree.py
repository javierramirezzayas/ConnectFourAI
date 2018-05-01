from DataStructures.node import Node


class Tree:

    def __init__(self):
        self.root = []
        self.children =[]
        self.numChildren = 0

    def insertNode(self, value, parent):
        node = Node(parent, value)
        if parent is not None:
            self.children.append(node)
        else:
            self.root = node
        self.numChildren = self.numChildren + 1
        return node

    def getRoot(self):
        return self.root

    def display(self):
        string0 = ''
        string1 = ''
        string2 = ''
        string3 = ''
        string4 = ''
        string5 = ''
        string6 = ''
        count = 0
        category = 0
        print('Root Node:')
        for row in self.root.getValue():
            print(row)
        for n in self.children:
            row = n.getValue()
            string0 = string0 + str(row[0]) + '   '
            string1 = string1 + str(row[1]) + '   '
            string2 = string2 + str(row[2]) + '   '
            string3 = string3 + str(row[3]) + '   '
            string4 = string4 + str(row[4]) + '   '
            string5 = string5 + str(row[5]) + '   '
            string6 = string6 + str(row[6]) + '   '
            count = count + 1
            if count==7:
                if category==0:
                    print('Max Nodes')
                else:
                    print('Min Nodes')
                print(string0)
                print(string1)
                print(string2)
                print(string3)
                print(string4)
                print(string5)
                print(string6)
                string0 = ''
                string1 = ''
                string2 = ''
                string3 = ''
                string4 = ''
                string5 = ''
                string6 = ''
                count = 0
                category = 1
    def getChildren(self,node):
        selectedChildren = []
        for child in self.children:
            if node.getValue() == child.getParent():
                selectedChildren.append(child)
        return selectedChildren

    def children(self):
        return self.children()
    def getNumberOfChildren(self):
        return self.numChildren

    def clear(self):
        del self.children
        del self.numChildren
        del self.root