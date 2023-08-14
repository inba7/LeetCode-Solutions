class Solution(object):
    def countAsterisks(self, s):
        Flag, Count = 0, 0
        for Char in s:
            if Char == "*" and Flag%2 == 0:
                Count += 1
            elif Char == "|":
                Flag += 1
        return Count