class Solution(object):
    def subtractProductAndSum(self, n):
        Prod, Sum = 1, 0
        while n>0:
            Prod *= n%10
            Sum += n%10
            n//=10
        return Prod - Sum