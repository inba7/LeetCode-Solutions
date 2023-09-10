class Solution(object):
    def __init__(self):
        self.dp = [[-1 for _ in range(505)] for _ in range(505)]
        self.MOD = 10**9 + 7
        
    def solve(self, np, nd):
        if np == 0 and nd == 0:
            return 1
        if np < 0 or nd < 0 or np > nd:
            return 0
        if self.dp[np][nd] != -1:
            return self.dp[np][nd]

        res = 0
        res = (res + np * self.solve(np - 1, nd)) % self.MOD
        res = (res + (nd - np) * self.solve(np, nd - 1)) % self.MOD
        self.dp[np][nd] = res
        return res

    def countOrders(self, n):
        return self.solve(n, n)