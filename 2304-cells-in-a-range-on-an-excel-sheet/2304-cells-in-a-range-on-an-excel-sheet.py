class Solution(object):
    def cellsInRange(self, s):
        Cells = []
        for col in range(ord(s[0]), ord(s[3])+1):
            for row in range(ord(s[1]), ord(s[4])+1):
                Cells.append(chr(col)+str(chr(row)))
        return Cells