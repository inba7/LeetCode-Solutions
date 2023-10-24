class Solution:
    def largestValues(self, root):
        self.Max = {}
        self.Find(root, Row=0)
        return list(self.Max.values())
    
    def Find(self, root, Row):
        if root == None:
            return
        if self.Max.get(Row, None) != None:
            self.Max[Row] = max(self.Max[Row], root.val)
        else:
            self.Max[Row] = root.val

        self.Find(root.left, Row+1)
        self.Find(root.right, Row+1)