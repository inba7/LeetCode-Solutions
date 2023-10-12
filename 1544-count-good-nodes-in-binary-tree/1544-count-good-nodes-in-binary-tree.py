class Solution(object):
    Res = 0
    def goodNodes(self, root):
        def DFS(node, CurrMax):
            if node.val >= CurrMax:
                CurrMax = node.val
                self.Res+=1
            if node.left:
                DFS(node.left, CurrMax)
            if node.right:
                DFS(node.right, CurrMax)
            return

        DFS(root,root.val)

        return self.Res