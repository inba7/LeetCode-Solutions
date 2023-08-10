class Solution(object):
    def minimumSum(self, num):
        Digits = []
        while num>0:
            Digits.append(num%10)
            num//=10
        Digits.sort()
        new1, new2 = Digits[0]*10+Digits[-1], Digits[1]*10+Digits[-2]
        return new1 + new2