class Solution(object):
    def isHappy(self, n):
        total = 0
        for digit in str(n):
            total += int(digit)**2
        
        seen = set()
        seen.add(total)
        while total != 1:
            new = 0
            for char in str(total):
                new += int(char)**2
            total = new
            if total in seen:
                return False
            seen.add(total)
        return True