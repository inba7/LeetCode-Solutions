class Solution(object):
    def removeDuplicateLetters(self, s):
        Check, N = {}, len(s)
        for x in range(N):
            Check[s[x]] = x

        Stack, Seen = [], set()
        for x in range(N):
            if s[x] not in Seen:
                while Stack and Stack[-1] > s[x] and Check[Stack[-1]] > x:
                    Seen.remove(Stack.pop())
                Stack.append(s[x])
                Seen.add(s[x])

        return "".join(Stack)