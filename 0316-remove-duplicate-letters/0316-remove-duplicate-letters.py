class Solution(object):
    def removeDuplicateLetters(self, s):
        Last = {Val:Idx for Idx, Val in enumerate(s)}

        Stack, Visited = [], set()
        for Idx, Val in enumerate(s):
            if Val not in Visited:
                while Stack and Stack[-1] > Val and Last[Stack[-1]] > Idx:
                    Visited.remove(Stack.pop())
                Stack.append(Val)
                Visited.add(Val)
        
        return "".join(Stack)