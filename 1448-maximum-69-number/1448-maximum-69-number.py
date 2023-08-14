class Solution(object):
    def maximum69Number (self, num):
        Temp = num
        N = len(str(num))-1
        while num > 0:
            if num//(10**N) != 9:
                break
            num%=10**N
            N-=1
        return Temp + 3*(10**N) if N > -1 else Temp