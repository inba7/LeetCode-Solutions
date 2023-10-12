class Solution(object):
    def longestZigZag(self, root):
        self.Max = 0

        def DFS(node, Left, Right):
            self.Max = max(self.Max, Left, Right)
            if node.left:
                DFS(node.left, Right + 1, 0)
            if node.right:
                DFS(node.right, 0, Left + 1)

        DFS(root, 0, 0)
        return self.Max