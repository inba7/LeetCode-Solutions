class Solution(object):
    def digitSum(self, s, k):
        while len(s) > k:
            new_s = ''
            for i in range(0,len(s), k):
                new_s += str(sum(int(d) for d in s[i:i+k]))
            s = new_s 
        return s