class Solution(object):
    def digitSum(self, s, k):
        if len(s) <= k:
            return s
        res = ""
        count = 0
        for i in range(0, len(s)):
            if i % k == 0 and i != 0:
                res += str(count)
                count = 0
            count += int(s[i])
        res += str(count)
        return self.digitSum(res, k)