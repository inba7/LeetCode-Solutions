class Solution(object):
    def romanToInt(self, s):
        Roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 
        'C': 100, 'D': 500, 'M': 1000}
        Total, Prev = 0, 0 
        for char in s:
            Current = Roman[char]
            if Current > Prev:
                Total += Current-2*Prev
            else:
                Total += Current
            Prev = Current
        return Total