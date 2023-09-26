class Solution(object):
    def removeDuplicateLetters(self, s):
        Check, N = {}, len(s)
        for x in range(N):
            Check[s[x]] = x

        Stack, Seen = [], set()
        for x in range(N):
            if s[x] in Seen: continue
            while Stack and Stack[-1] > s[x] and Check[Stack[-1]] > x:
                Seen.remove(Stack[-1])
                Stack.pop()
            Seen.add(s[x])
            Stack.append(s[x])
        return "".join(Stack)