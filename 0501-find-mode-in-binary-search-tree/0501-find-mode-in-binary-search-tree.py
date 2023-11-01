class Solution(object):
    def findMode(self, root):
        def mode(root, m):
            if not root: return
            if root.val not in m:
                m[root.val] = 0
            m[root.val] += 1
            mode(root.left, m)
            mode(root.right, m)
            return
        m = {}
        mode(root, m)
        res = []
        mx = float("-inf")
        for k,v in m.items():
            if v > mx:
                res = [k]
                mx = v
            elif v == mx:
                res.append(k)
        return res



        