class Tree:

    def __init__(self, val=0, next=[]):
        self.val = val
        self.next = next
    
    def addNode(self, child_val):
        child = Tree(child_val, [])
        self.next.append(child)
