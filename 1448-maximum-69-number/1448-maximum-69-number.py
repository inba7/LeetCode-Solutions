class Solution(object):
    def maximum69Number (self, num):
        Num = str(num)
        New = ''
        N = len(Num)
        Max = 0
        for x in range(N):
            if Num[x] == '6' and Max == 0:
                New += '9'
                Max = 1
            else:
                New += Num[x]
        return int(New)