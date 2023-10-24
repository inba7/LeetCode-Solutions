class Solution(object):
    def twoOutOfThree(self, n1, n2, n3):
        return set(n1) & set(n2) | set(n2) & set(n3) | set(n1) & set(n3)