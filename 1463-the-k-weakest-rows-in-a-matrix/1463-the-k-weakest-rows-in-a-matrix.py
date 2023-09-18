class Solution(object):
    def kWeakestRows(self, mat, k):
        m = range(len(mat))
        rows = sorted(m, key=lambda i: mat[i])
        del rows[k:]
        return rows