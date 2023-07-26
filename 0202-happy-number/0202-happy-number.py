class Solution(object):
    def isHappy(self, n):
        visit = set()
        while n not in visit:
            visit.add(n)
            n= self.sumSquered(n)
            if n == 1:
                return True
        return False
    
    def sumSquered(self, n):
        output= 0
        while n:
            digit = n%10
            digit = digit ** 2
            output += digit
            n = n//10
        return output