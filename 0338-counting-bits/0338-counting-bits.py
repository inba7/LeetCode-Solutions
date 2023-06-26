class Solution(object):
    def countBits(self, n):
        ans = [0]*(n+1)
        for i in range(1,n+1):
            q,r=i,0
            while (q>=1):
                r=q%2
                if r==1: ans[i]+=1
                q//=2
            ans[i]+=q
        return ans