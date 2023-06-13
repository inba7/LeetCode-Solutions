class Solution(object):
    def myAtoi(self, s):
        s = s.strip()  # Remove leading and trailing whitespace
        if not s:
            return 0  # Handle empty string case
        Num = 0
        i = 0
        Sign = 1  # 1 for positive, -1 for negative
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            i += 1
            Sign = -1
        while i < len(s) and s[i].isdigit():
            Num = Num * 10 + int(s[i])
            i += 1
        Num *= Sign
        Num = max(min(Num, 2 ** 31 - 1), -2 ** 31)
        return Num