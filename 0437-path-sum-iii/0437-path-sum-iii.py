class Solution(object):
    def pathSum(self, root, targetSum):
        def DFS(node, target, Total):
            if not node:
                return 0

            Total += node.val
            old_total = Total - target
            self.result += cache.get(old_total, 0)
            cache[Total] = cache.get(Total, 0) + 1

            DFS(node.left, target, Total)
            DFS(node.right, target, Total)

            cache[Total] -= 1         
        
        cache = {0:1}
        self.result = 0
        DFS(root, targetSum, 0)
        return self.result