class Solution(object):
    def countDigits(self, num):
        Count = 0
        for val in str(num):
            if num%int(val)==0:
                Count+=1
        return Count