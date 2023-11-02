class Solution:
    def __init__(self):
        self.matchingSubtreeCount = 0 
    
    def calculateSubtreeValues(self, currentNode):
        if currentNode is None:
            return 0, 0
        leftSubtree  = self.calculateSubtreeValues(currentNode.left)
        rightSubtree = self.calculateSubtreeValues(currentNode.right)

        Values  = leftSubtree [0] + rightSubtree[0] + currentNode.val
        Nodes  = leftSubtree [1] + rightSubtree[1] + 1

        if Nodes != 0 and Values // Nodes == currentNode.val:
            self.matchingSubtreeCount += 1
        return Values, Nodes 

    def averageOfSubtree(self, root):
        self.calculateSubtreeValues(root)
        return self.matchingSubtreeCount 