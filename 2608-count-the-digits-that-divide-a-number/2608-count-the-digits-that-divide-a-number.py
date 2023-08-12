class Solution(object):
    def countDigits(self, num):
        Temp = num
        Count = 0
        while Temp>0:
            if num%(Temp%10)==0:
                Count+=1
            Temp//=10
        return Count