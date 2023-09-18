class Solution(object):
    def kWeakestRows(self, mat, k):
        M = range(len(mat))
        Rows = sorted(M, key=lambda i: mat[i])
        del Rows[k:]
        return Rows