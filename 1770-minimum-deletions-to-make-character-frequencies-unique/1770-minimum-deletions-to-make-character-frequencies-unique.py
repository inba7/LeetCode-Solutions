class Solution(object):
    def minDeletions(self, s):
        res = {i:s.count(i) for i in set(s)}
        counter = 0
        unique = []
        for k, v in res.items():
            while v > 0 and v in unique:
                v-=1
                counter+=1
            unique.append(v)
        return counter 