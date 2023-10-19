class Solution(object):
    def backspaceCompare(self, s, t):
        S, T = [], []
        for X in s:
            if X == "#" and S:
                S.pop()
            elif X != "#":
                S.append(X)

        for Y in t:
            if Y == "#" and T:
                T.pop()
            elif Y != "#":
                T.append(Y)

        return S == T