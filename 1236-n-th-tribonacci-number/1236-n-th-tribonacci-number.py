class Solution(object):
    def tribonacci(self, n):
        trib = 0
        first, second= 0, 1
        third = first+second
        if n == 0: 
            return first
        elif n == 1: 
            return second
        elif n == 2:
            return third
        else:
            for i in range(2,n):
                trib = first + second + third
                first = second
                second = third
                third = trib
            return trib