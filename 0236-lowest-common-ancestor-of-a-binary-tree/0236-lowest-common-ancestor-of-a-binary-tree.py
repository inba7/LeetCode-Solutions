class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root or p == root or q == root:
            return root

        Left = self.lowestCommonAncestor(root.left, p, q)
        Right = self.lowestCommonAncestor(root.right, p, q)
        if Left and Right: 
            return root
        elif Left: 
            return Left
        else: 
            return Right