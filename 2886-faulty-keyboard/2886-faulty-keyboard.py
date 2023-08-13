class Solution(object):
    def finalString(self, s):
        S = ""
        for char in s:
            if char == 'i':
                S = S[::-1]
            else:
                S += char
        return S