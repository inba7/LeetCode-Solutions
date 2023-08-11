class Solution(object):
    def balancedStringSplit(self, s):
        Bal = Count = 0
        for X in s:
            Bal += 1 if X == "R" else -1
            if Bal == 0:
                Count += 1
        return Count