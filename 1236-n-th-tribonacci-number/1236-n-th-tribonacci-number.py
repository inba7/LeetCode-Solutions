class Solution(object):
    def tribonacci(self, n):
        if n == 0: 
            return 0
        elif (n == 1 or n ==2):
            return 1
        else:
            trib = 0
            first, second= 0, 1
            third = first+second
            for i in range(2,n):
                trib = first + second + third
                first = second
                second = third
                third = trib
            return trib