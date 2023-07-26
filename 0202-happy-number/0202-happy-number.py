class Solution(object):
    def nextNumber(self, n):
        newNumber = 0
        while n != 0:
            num = n % 10
            newNumber += num * num
            n = n / 10
        return newNumber

    def isHappy(self, n):
        s = set()
        while n != 1 and n not in s:
            s.add(n)
            n = self.nextNumber(n)
        return n == 1