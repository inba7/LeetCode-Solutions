class Solution(object):
    def searchBST(self, root, val):
        Current = root
        while Current != None:
            if Current.val == val: return Current
            if Current.val > val: Current = Current.left
            else: Current = Current.right
        return Current