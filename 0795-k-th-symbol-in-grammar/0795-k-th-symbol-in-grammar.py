class Solution(object):
    s = [1,0]
    def kthGrammar(self, n, k):
        if k < 2: return self.s[k]
        for i in range(1, n):
            if k <= 2**i:
                if i%2 == 0: return self.kthGrammar(n, 2**i-k+1)
                else: return (self.kthGrammar(n, 2**i-k+1)+1) % 2