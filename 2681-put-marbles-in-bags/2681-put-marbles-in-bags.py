class Solution(object):
    def putMarbles(self, weights, k):
        i=0
        j=0
        l=[]
        for j in range(len(weights)-1):
            sum=weights[j]+weights[j+1]
            l.append(sum)
            sum=0
        l.sort()
        p=len(l)-1
        sum1=0
        sum2=0
        while k>1:
            sum1=sum1+l[i]
            sum2=sum2+l[p]
            i=i+1
            p=p-1
            k=k-1
        return sum2-sum1