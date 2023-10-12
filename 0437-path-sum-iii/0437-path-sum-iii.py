class Solution(object):
    def pathSum(self, root, targetSum):
        self.count = 0
        self.prefix_sum = {0: 1}
        self.dfs(root, targetSum, 0)
        return self.count
        
    def dfs(self, node, targetSum, CurrSum):
        if not node:
            return
        
        CurrSum += node.val
        self.count += self.prefix_sum.get(CurrSum - targetSum, 0)
        self.prefix_sum[CurrSum] = self.prefix_sum.get(CurrSum, 0) + 1
        
        self.dfs(node.left, targetSum, CurrSum)
        self.dfs(node.right, targetSum, CurrSum)
        
        self.prefix_sum[CurrSum] -= 1