class Solution(object):
    def smallestSubsequence(self, s):
        Last = {}
        for x in range(len(s)):
            Last[s[x]] = x

        Stack, Visited = [], set()
        for x in range(len(s)):
            if s[x] not in Visited:
                while Stack and Stack[-1] > s[x] and Last[Stack[-1]] > x:
                    Visited.remove(Stack.pop())
                Stack.append(s[x])
                Visited.add(s[x])
        
        return "".join(Stack) 