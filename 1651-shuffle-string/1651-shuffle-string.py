class Solution(object):
    def restoreString(self, s, indices):
        if indices == sorted(indices):
            return s
        S = list(s)
        ZP = zip(indices, S)
        Z = [val for key, val in sorted(ZP)]
        return "".join(Z)