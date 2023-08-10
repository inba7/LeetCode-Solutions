class Solution(object):
    def subtractProductAndSum(self, n):
        Prod, Sum = 1, 0
        while n>0:
            Digit = n%10
            Prod *= Digit
            Sum += Digit
            n//=10
        return Prod - Sum