class Solution(object):
    def numberOfSteps(self, num):
        Count = 0
        while num > 0:
            if (num%2==0):
                num/=2
            else:
                num-=1
            Count += 1
        return Count