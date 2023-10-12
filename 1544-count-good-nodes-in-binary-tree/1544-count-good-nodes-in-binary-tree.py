class Solution(object):
    def goodNodes(self, root):
        if not root:
            return 0
        
        def dfs(node, currMax):
            if not node:
                return
            if node.val >= currMax:
                Count[0] += 1
                currMax = node.val
            dfs(node.left, currMax)
            dfs(node.right, currMax)
        
        Count = [0]
        dfs(root, root.val)
        
        return Count[0]