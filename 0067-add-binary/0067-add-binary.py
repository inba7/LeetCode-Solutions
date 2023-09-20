class Solution(object):
    def addBinary(self, a, b):
        total = int(a,2) + int(b,2)
        return "{:b}".format(total)