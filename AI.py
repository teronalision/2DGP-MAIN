import ENGINE


class Tree:
    SUCCESS, RUNNING, FAIL = 1, 0, -1
    def __init__(self, root):
        self.root = root

    def run(self):
        self.root.run()

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name
        self.pre_running = 0

    def add_child(self, c):
        self.children.append(c)
    def add_children(self, *c):
        for child in c:
            self.children.append(child)

class SelectNode(Node):
    def __init__(self, name):
        self.Node.__init__(name)

    def run(self):
        for pos in range(self.pre_running, len(self.children)):
            result = self.children[pos].run()
            if (result == Tree.RUNNING):
                self.pre_running = pos
                return Tree.RUNNING
            elif (result == Tree.SUCCESS):
                self.pre_running = 0
                return Tree.SUCCESS
        self.pre_running = 0
        return Tree.FAIL

class SequenceNode(Node):
    def __init__(self, name):
        self.Node.__init__(name)

    def run(self):
        for pos in range(self.pre_running, len(self.children)):
            result = self.children[pos].run()
            if (result == Tree.RUNNING):
                self.pre_running = pos
                return Tree.RUNNING
            elif (result == Tree.FAIL):
                self.pre_running = 0
                return Tree.FAIL
        self.pre_running = 0
        return Tree.SUCCESS

class LeafNode(Node):
    def __init__(self,name,func):
        self.name = name
        self.func = func

    def run(self):
        return self.func()