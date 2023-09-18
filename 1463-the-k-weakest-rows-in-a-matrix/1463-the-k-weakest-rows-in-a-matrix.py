class Solution(object):
    def kWeakestRows(self, mat, k):
        Res = [x for x in range(len(mat))]
        Count = []
        for row in mat:
            Count.append(row.count(1))
        ZP = zip(Count, Res)
        Zip = [row for count, row in sorted(ZP)]
        return Zip[:k]