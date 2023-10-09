class Solution(object):
    def minEatingSpeed(self, piles, h):
        if h==len(piles):
            return max(piles)
     
        s=sum(piles)
        mini=s/h+1 if s%h>0 else s/h
        maxi=s/(h-len(piles)+1)+1
 
        return self.binary_search(mini,maxi, h, piles)

    def binary_search(self, mini,maxi, h, piles):
        while mini!=maxi:
            mid=(mini+maxi)/2
            if self.can_finish(piles,mid)<=h:
                maxi=mid
            else:
                mini=mid+1

        return mini

    def can_finish(self,piles,k):
        r=0
        for pile in piles:
            r+=pile/k
            if pile%k>0:
                r+=1
        return r