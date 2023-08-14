class Solution(object):
    def minOperations(self, n):
        return (n/2)**2 if n%2==0 else (n//2)*(n//2+1)