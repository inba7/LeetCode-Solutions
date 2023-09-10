class Solution(object):
    def countOrders(self, n):
        res=1
        mod=10**9+7
        for i in range(2,n+1):
            res=res*(2*i-1)*2*i//2 % mod
        return res