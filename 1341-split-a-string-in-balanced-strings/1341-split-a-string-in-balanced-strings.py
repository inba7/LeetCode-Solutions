class Solution(object):
    def balancedStringSplit(self, s):
        Count = 0
        Left, Right = 0, 0
        for i in range(len(s)):
            if s[i] == 'R':
                Right += 1
            else:
                Left += 1
            if Right == Left:
                Count += 1
        return Count