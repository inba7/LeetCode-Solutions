class Solution(object):
    def findMode(self, root):
        maxv = {'max':0}
        hashmap = {}
        def dfs(root, parent, freq):
            if root == None:
                return
            if root.val not in hashmap:
                hashmap[root.val] = 0
            hashmap[root.val] += 1
            if hashmap[root.val] > maxv['max']:
                maxv['max'] = hashmap[root.val]
            if root.left:
                dfs(root.left, root.val, freq)
            if root.right:
                dfs(root.right, root.val, freq)

        dfs(root, 0, 0)
        res = []
        for key,value in hashmap.items():
            if value == maxv['max']:
                res.append(key)
        return res