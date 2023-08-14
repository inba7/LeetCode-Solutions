class Solution(object):
    def maximum69Number (self, num):
        Num = list(str(num))
        for N in range(len(Num)):
            if Num[N] == '6':
                Num[N] = '9'
                break
        return int("".join(Num))