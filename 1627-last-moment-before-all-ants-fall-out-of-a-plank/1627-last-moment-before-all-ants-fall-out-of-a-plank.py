class Solution(object):
    def getLastMoment(self, n, left, right):
        left.append(0)
        right.append(n)        
        
        return max(max(left), n - min(right))