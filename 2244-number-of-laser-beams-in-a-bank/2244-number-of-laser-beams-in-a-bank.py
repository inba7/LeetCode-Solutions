class Solution(object):
    def numberOfBeams(self, bank):
        Beams, Prev = 0, 0
        for row in bank:
            Current = row.count('1')
            if Current:
                Beams += Prev * Current
                Prev = Current
        return Beams