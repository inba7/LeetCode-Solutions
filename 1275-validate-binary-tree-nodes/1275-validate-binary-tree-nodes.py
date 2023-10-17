class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        Parents = {}
        for Parent, Child in enumerate(zip(leftChild,rightChild)):
            for C in Child:
                if C == -1:
                    continue 
                if C in Parents:
                    return False 
                if Parent in Parents and Parents[Parent] == C:
                    return False 
                Parents[C]=Parent
        
        def Count(root):
            if root ==-1:
                return 0
            return 1 + Count(leftChild[root]) + Count(rightChild[root])
        
        root = set(range(n)) - set(Parents.keys())
        if  len(root)!=1:
            return False 
        
        return Count(root.pop()) == n